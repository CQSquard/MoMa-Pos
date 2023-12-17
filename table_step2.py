# The step2 aims to shinengchang
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
all_boxes_range=[[[0.249, 0.499, 0.774], [1.751, 0.499, 0.774], [1.751, 1.501, 0.774], [0.249, 1.501, 0.774], [0.249, 0.499, 0.8260000000000001], [1.751, 0.499, 0.8260000000000001], [1.751, 1.501, 0.8260000000000001], [0.249, 1.501, 0.8260000000000001]], [[0.29899999999999993, 0.5489999999999999, -0.18600000000000005], [0.401, 0.5489999999999999, -0.18600000000000005], [0.401, 0.651, -0.18600000000000005], [0.29899999999999993, 0.651, -0.18600000000000005], [0.29899999999999993, 0.5489999999999999, 0.7659999999999999], [0.401, 0.5489999999999999, 0.7659999999999999], [0.401, 0.651, 0.7659999999999999], [0.29899999999999993, 0.651, 0.7659999999999999]], [[0.29899999999999993, 1.349, -0.18600000000000005], [0.401, 1.349, -0.18600000000000005], [0.401, 1.4509999999999998, -0.18600000000000005], [0.29899999999999993, 1.4509999999999998, -0.18600000000000005], [0.29899999999999993, 1.349, 0.7659999999999999], [0.401, 1.349, 0.7659999999999999], [0.401, 1.4509999999999998, 0.7659999999999999], [0.29899999999999993, 1.4509999999999998, 0.7659999999999999]], [[1.5989999999999998, 0.5489999999999999, -0.18600000000000005], [1.701, 0.5489999999999999, -0.18600000000000005], [1.701, 0.651, -0.18600000000000005], [1.5989999999999998, 0.651, -0.18600000000000005], [1.5989999999999998, 0.5489999999999999, 0.7659999999999999], [1.701, 0.5489999999999999, 0.7659999999999999], [1.701, 0.651, 0.7659999999999999], [1.5989999999999998, 0.651, 0.7659999999999999]], [[1.5989999999999998, 1.349, -0.18600000000000005], [1.701, 1.349, -0.18600000000000005], [1.701, 1.4509999999999998, -0.18600000000000005], [1.5989999999999998, 1.4509999999999998, -0.18600000000000005], [1.5989999999999998, 1.349, 0.7659999999999999], [1.701, 1.349, 0.7659999999999999], [1.701, 1.4509999999999998, 0.7659999999999999], [1.5989999999999998, 1.4509999999999998, 0.7659999999999999]]]


fig, ax = plt.subplots()

# 定义一个函数来提取在z=0.85平面的边
def get_edges_at_z(box, z_value):
    # 提取每个盒子的底部和顶部角点
    bottom_corners = box[:4]
    top_corners = box[4:]

    # 存储在z=0.85平面上的边
    edges_on_plane = []

    # 检查每一对底部和顶部角点
    for b, t in zip(bottom_corners, top_corners):
        # 如果一个角点在平面下方，另一个在上方，则边与平面相交
        if (b[2] <= z_value and t[2] >= z_value) or (b[2] >= z_value and t[2] <= z_value):
            # 使用线性插值找到交点
            ratio = (z_value - b[2]) / (t[2] - b[2])
            x = b[0] + ratio * (t[0] - b[0])
            y = b[1] + ratio * (t[1] - b[1])
            edges_on_plane.append([x, y])

    return edges_on_plane
all_edges_on_plane = []
# 处理每个盒子并在z=0.85平面绘制边
for box in all_boxes_range:
    edges = get_edges_at_z(box, 0.8)
    if edges:
        # 假设每个盒子在平面上有两条边
        polygon = Polygon(edges, closed=False, edgecolor='r', fill=None)
        ax.add_patch(polygon)
        all_edges_on_plane.append(edges)
print(all_edges_on_plane)
# 在z=0.85平面上添加散点图点（4.2, 5.5）
ax.scatter(1, 1, color='green')

# 设置图的限制
ax.set_xlim(-1, 3)
ax.set_ylim(-1, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Z=0.8 touying')

# 展示图表
plt.show()
