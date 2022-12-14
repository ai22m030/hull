import numpy as np
import matplotlib.pyplot as plt
import math
from timeit import Timer


# This function simple generates a list of coordinates
def generate_k_xy(k):
    xy = np.random.rand(k, 2)
    return xy


# Navigate around the hull to find the top/bottom tanget
def find_tangent(xy_left, xy_right):
    return 0


# Merge hulls
def hull_merge(xy_left, xy_right, isinitial):
    # Identify the indexes of the rightmost point on the left hull and vice versa
    rightmost_lefthull = np.where(xy_left[:, 0] == np.max(xy_left[:, 0], axis=0))[0][0]
    leftmost_righthull = np.where(xy_right[:, 0] == np.min(xy_right[:, 0], axis=0))[0][0]

    # Sort the arrays clockwise if it's the first (isinitial), the hulls returned from this merge are already sorted
    # clockwise
    if isinitial:
        # This clockwise sorting is only required for hulls with 3 points
        placeholder_left = []
        if len(xy_left) == 3:
            placeholder_left.append(xy_left[rightmost_lefthull])
            a = (xy_left[rightmost_lefthull] - xy_left[rightmost_lefthull - 1])
            b = (xy_left[rightmost_lefthull] - xy_left[rightmost_lefthull - 2])
            angle_between_vectors = np.cross(a, b)
            if angle_between_vectors > 0:
                placeholder_left.append(xy_left[rightmost_lefthull - 2])
                placeholder_left.append(xy_left[rightmost_lefthull - 1])
            elif angle_between_vectors < 0:
                placeholder_left.append(xy_left[rightmost_lefthull - 1])
                placeholder_left.append(xy_left[rightmost_lefthull - 2])
            # When the angle is 0, remove the middle point
            else:
                if np.linalg.norm(a) > np.linalg.norm(b):
                    placeholder_left.append(xy_left[rightmost_lefthull - 1])
                else:
                    placeholder_left.append(xy_left[rightmost_lefthull - 2])

            xy_left = np.array(placeholder_left)
            rightmost_lefthull = 0

        placeholder_right = []
        if len(xy_right) == 3:
            placeholder_right.append(xy_right[leftmost_righthull])
            a = (xy_right[leftmost_righthull] - xy_right[leftmost_righthull - 1])
            b = (xy_right[leftmost_righthull] - xy_right[leftmost_righthull - 2])
            angle_between_vectors = np.cross(a, b)
            if angle_between_vectors > 0:
                placeholder_right.append(xy_right[leftmost_righthull - 2])
                placeholder_right.append(xy_right[leftmost_righthull - 1])
            elif angle_between_vectors < 0:
                placeholder_right.append(xy_right[leftmost_righthull - 1])
                placeholder_right.append(xy_right[leftmost_righthull - 2])
            # When the angle is 0, remove the middle point
            else:
                if np.linalg.norm(a) > np.linalg.norm(b):
                    placeholder_left.append(xy_left[rightmost_lefthull - 1])
                else:
                    placeholder_left.append(xy_left[rightmost_lefthull - 2])

            xy_right = np.array(placeholder_right)
            leftmost_righthull = 0

    search_top, search_p, search_q = True, True, True
    p_top = rightmost_lefthull
    q_top = leftmost_righthull
    # Find top tangent
    while search_top:
        org_angle = False
        # Navigate up the right hull clockwise (moving q)
        while search_q:
            new_angle = np.arctan2(xy_right[q_top][1] - xy_left[p_top][1], xy_right[q_top][0] - xy_left[p_top][0])
            if org_angle == False:
                q_top = (q_top + 1) % len(xy_right)
                org_angle = new_angle
            # If the new angle is greater, check the next point on the right hull clockwise
            elif org_angle < new_angle:
                q_top = (q_top + 1) % len(xy_right)
                org_angle = new_angle
                # If we moved the point q, we need to check point p again
                search_p = True
            # If the new angle is smaller, this implies that the previous point was the current top tangent point q
            else:
                q_top = (q_top - 1) % len(xy_right)
                search_q = False

        org_angle = False
        # Navigate up the lef hull counter clockwise (moving p)
        while search_p:
            new_angle = np.arctan2(xy_right[q_top][1] - xy_left[p_top][1], xy_right[q_top][0] - xy_left[p_top][0])
            if not org_angle:
                p_top = (p_top - 1) % len(xy_left)
                org_angle = new_angle
            # If the new angle is smaller, check the next point on the right hull clockwise
            elif org_angle > new_angle:
                p_top = (p_top - 1) % len(xy_left)
                org_angle = new_angle
                # If we moved the point p, we need to check point q again
                search_q = True
            # If the new angle is greater, this implies that the previous point was the current top tangent point q
            else:
                p_top = (p_top + 1) % len(xy_left)
                search_p = False

        if search_q == False and search_p == False:
            search_top = False

    search_bot, search_p, search_q = True, True, True
    p_bot = rightmost_lefthull
    q_bot = leftmost_righthull
    # Find bottom tangent
    while search_bot == True:
        org_angle = False
        # Navigate up the right hull clockwise (moving q)
        while search_q == True:
            new_angle = np.arctan2(xy_right[q_bot][1] - xy_left[p_bot][1], xy_right[q_bot][0] - xy_left[p_bot][0])
            if org_angle == False:
                q_bot = (q_bot - 1) % len(xy_right)
                org_angle = new_angle
            # If the new angle is smaller , check the next point on the right hull counter clockwise
            elif org_angle > new_angle:
                q_bot = (q_bot - 1) % len(xy_right)
                org_angle = new_angle
                # If we moved the point q, we need to check point p again
                search_p = True
            # If the new angle is smaller, this implies that the previous point was the current top tangent point q
            else:
                q_bot = (q_bot + 1) % len(xy_right)
                search_q = False

        org_angle = False
        # Navigate up the lef hull counter clockwise (moving p)
        while search_p == True:
            new_angle = np.arctan2(xy_right[q_bot][1] - xy_left[p_bot][1], xy_right[q_bot][0] - xy_left[p_bot][0])
            if org_angle == False:
                p_bot = (p_bot + 1) % len(xy_left)
                org_angle = new_angle
            # If the new angle is greater, check the next point on the right hull clockwise
            elif org_angle < new_angle:
                p_bot = (p_bot + 1) % len(xy_left)
                org_angle = new_angle
                # If we moved the point p, we need to check point q again
                search_q = True
            # If the new angle is greater, this implies that the previous point was the current top tangent point q
            else:
                p_bot = (p_bot - 1) % len(xy_left)
                search_p = False

        if search_q == False and search_p == False:
            search_bot = False

    # Stack the points into a hull clockwise
    if q_top > q_bot:
        if p_top > p_bot:
            result = np.vstack((xy_left[p_top], xy_right[q_top:], xy_right[:q_bot + 1], xy_left[p_bot:p_top]))
        elif p_top < p_bot:
            result = np.vstack((xy_left[:p_top + 1], xy_right[q_top:], xy_right[:q_bot + 1], xy_left[p_bot:]))
        # If p_top == p_bot (the same indice) this implies that the other points are surround by the hull and
        # shouldn't be inlcuded
        else:
            result = np.vstack((xy_left[p_top], xy_right[q_top:], xy_right[:q_bot + 1]))
    elif q_top < q_bot:
        if p_top > p_bot:
            result = np.vstack((xy_left[p_top], xy_right[q_top:q_bot + 1], xy_left[p_bot:p_top]))
        elif p_top < p_bot:
            result = np.vstack((xy_left[:p_top + 1], xy_right[q_top:q_bot + 1], xy_left[p_bot:]))
            # If p_top == p_bot (the same indice) this implies that the other points are surround by the hull and
            # shouldn't be inlcuded
        else:
            result = np.vstack((xy_left[p_top], xy_right[q_top:q_bot + 1]))
    # If q_top == q_bot (the same indice) this implies that the other points are surround by the hull and shouldn't
    # be included
    else:
        if p_top > p_bot:
            result = np.vstack((xy_left[p_top], xy_right[q_top], xy_left[p_bot:p_top]))
        elif p_top < p_bot:
            result = np.vstack((xy_left[:p_top + 1], xy_right[q_top], xy_left[p_bot:]))
            # If p_top == p_bot (the same indices) this implies that the other points are surround by the hull and
            # shouldn't be included
        # Note: This case will never happen because this implies that both the left and the right hull surround
        # each other because this is just a line
        else:
            result = np.vstack((xy_left[p_top], xy_right[q_top]))

    return result


# Recursively calculates the hulls (starting from a line or triangle)
merge_hulls = {}


def convex_hull(xy, recursion_level):
    global merge_hulls
    if str(recursion_level) not in merge_hulls:
        merge_hulls[str(recursion_level)] = []
    if len(xy) <= 3:
        merge_hulls[str(recursion_level)].append(xy)
        return xy, True
    left_half, isinitial = convex_hull(xy[0: int(math.ceil(len(xy) / 2))], recursion_level + 1)
    right_half, isinitial = convex_hull(xy[int(math.ceil(len(xy) / 2)):], recursion_level + 1)
    hull_merge_it = hull_merge(left_half, right_half, isinitial)
    merge_hulls[str(recursion_level)].append(hull_merge_it)
    return hull_merge_it, False


# If run from this file
if __name__ == "__main__":
    app_mode = 99
    k = 100

    while not (app_mode == 0 or app_mode == 1):
        print("\nChose the algorithm mode:\n")
        try:
            app_mode = int(input("0 - speed mode, 1 - graphics mode: "))
        except:
            print("wrong input")

    try:
        k = int(input("How many data points shall be created (default 100) : ") or 100)
    except:
        print("wrong input, proceeding with default")

    # Input coordination

    # for k in range(1001,10001):
    xy = generate_k_xy(k)
    xy = xy[xy[:, 0].argsort()]

    t = Timer(lambda: convex_hull(xy, 0))
    # Save the time-required to the file "o_notationdata.txt"
    matrix = np.loadtxt('o_notation_data_dc.txt')
    # Find the current time value for a specific k (note that k is stored in the first column)
    k_index = np.where(matrix[:, 0] == k)[0]
    if k_index.size == 0:
        matrix = np.vstack((matrix, [k, t.timeit(number=1)]))
    else:
        # Get average value between current and previous
        matrix[k_index[0]][1] = (matrix[k_index[0]][1] + t.timeit(number=1)) / 2
    with open('o_notation_data_dc.txt', 'wb') as f:
        np.savetxt(f, matrix, delimiter=' ')

    if app_mode == 1:
        # Plot everything
        import imageio

        plt.figure()
        plt.scatter(xy[:, 0], xy[:, 1], color='grey')
        # plt.show()

        for keys in merge_hulls:
            fig, ax = plt.subplots(1, 1)
            for hulls in merge_hulls[keys]:
                hulls_temp = np.vstack((hulls, hulls[0]))
                plt.scatter(xy[:, 0], xy[:, 1], color='grey')
                ax.plot(hulls_temp[:, 0], hulls_temp[:, 1])
            plt.savefig(f'png_images/line-{keys}.png')
            plt.close()

        frams = []
        with imageio.get_writer('line.gif', mode='i', fps=1) as writer:
            for i in range(len(merge_hulls) - 1, -1, -1):
                image = imageio.imread(f'png_images/line-{i}.png')
                writer.append_data(image)

        plt.show()
    else:
        print(merge_hulls['0'])

    print('Time (s): ' + str(t.timeit(number=1)))
