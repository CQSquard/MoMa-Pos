# 这段代码的all_boxes_range来源于relvolute.py中的all_boxes_range,这一步的目的是再现我所要建立势能场的背景
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
#all_boxes_range=[[[4.098999999999999, 5.419, 1.054], [4.101, 5.419, 1.054], [4.101, 5.421, 1.054], [4.098999999999999, 5.421, 1.054], [4.098999999999999, 5.419, 1.0559999999999998], [4.101, 5.419, 1.0559999999999998], [4.101, 5.421, 1.0559999999999998], [4.098999999999999, 5.421, 1.0559999999999998]], [[3.1862777365475883, 5.069626060035825, 0.32445440387725766], [3.833652749660611, 5.069626060035825, 0.32445440387725766], [3.833652749660611, 5.10759665825665, 0.32445440387725766], [3.1862777365475883, 5.10759665825665, 0.32445440387725766], [3.1862777365475883, 5.069626060035825, 1.9208873894214626], [3.833652749660611, 5.069626060035825, 1.9208873894214626], [3.833652749660611, 5.10759665825665, 1.9208873894214626], [3.1862777365475883, 5.10759665825665, 1.9208873894214626]], [[3.211781252744793, 4.954778346326948, 0.9621310020089143], [3.245482742789387, 4.954778346326948, 0.9621310020089143], [3.245482742789387, 4.991910760191083, 0.9621310020089143], [3.211781252744793, 4.991910760191083, 0.9621310020089143], [3.211781252744793, 4.954778346326948, 1.3775105144977564], [3.245482742789387, 4.954778346326948, 1.3775105144977564], [3.245482742789387, 4.991910760191083, 1.3775105144977564], [3.211781252744793, 4.991910760191083, 1.3775105144977564]], [[3.8342374981641765, 5.682189099311828, 0.015757085800170767], [4.409681093573571, 5.682189099311828, 0.015757085800170767], [4.409681093573571, 5.74132460463047, 0.015757085800170767], [3.8342374981641765, 5.74132460463047, 0.015757085800170767], [3.8342374981641765, 5.682189099311828, 2.049774296760559], [4.409681093573571, 5.682189099311828, 2.049774296760559], [4.409681093573571, 5.74132460463047, 2.049774296760559], [3.8342374981641765, 5.74132460463047, 2.049774296760559]], [[3.8342374981641756, 5.095949591517448, 0.015757085800170767], [4.40968109357357, 5.095949591517448, 0.015757085800170767], [4.40968109357357, 5.158115598142147, 0.015757085800170767], [3.8342374981641756, 5.158115598142147, 0.015757085800170767], [3.8342374981641756, 5.095949591517448, 2.049774296760559], [4.40968109357357, 5.095949591517448, 2.049774296760559], [4.40968109357357, 5.158115598142147, 2.049774296760559], [3.8342374981641756, 5.158115598142147, 2.049774296760559]], [[3.834237498164176, 5.135198701739311, 1.8739398140907284], [4.409681093573569, 5.135198701739311, 1.8739398140907284], [4.409681093573569, 5.701363785147667, 1.8739398140907284], [3.834237498164176, 5.701363785147667, 1.8739398140907284], [3.834237498164176, 5.135198701739311, 2.049774296760559], [4.409681093573569, 5.135198701739311, 2.049774296760559], [4.409681093573569, 5.701363785147667, 2.049774296760559], [3.834237498164176, 5.701363785147667, 2.049774296760559]], [[3.834237498164177, 5.135198701739311, 0.015757085800170517], [4.409681093573571, 5.135198701739311, 0.015757085800170517], [4.409681093573571, 5.701363785147667, 0.015757085800170517], [3.834237498164177, 5.701363785147667, 0.015757085800170517], [3.834237498164177, 5.135198701739311, 0.3738451318740845], [4.409681093573571, 5.135198701739311, 0.3738451318740845], [4.409681093573571, 5.701363785147667, 0.3738451318740845], [3.834237498164177, 5.701363785147667, 0.3738451318740845]], [[4.393690905094146, 5.135198701739311, 0.01575708580017121], [4.40968109357357, 5.135198701739311, 0.01575708580017121], [4.40968109357357, 5.701363785147667, 0.01575708580017121], [4.393690905094146, 5.701363785147667, 0.01575708580017121], [4.393690905094146, 5.135198701739311, 2.049774296760559], [4.40968109357357, 5.135198701739311, 2.049774296760559], [4.40968109357357, 5.701363785147667, 2.049774296760559], [4.393690905094146, 5.701363785147667, 2.049774296760559]], [[3.8731993994712823, 5.134198701739311, 0.7832930037975309], [4.400690905094146, 5.134198701739311, 0.7832930037975309], [4.400690905094146, 5.702363785147667, 0.7832930037975309], [3.8731993994712823, 5.702363785147667, 0.7832930037975309], [3.8731993994712823, 5.134198701739311, 0.8234811943173409], [4.400690905094146, 5.134198701739311, 0.8234811943173409], [4.400690905094146, 5.702363785147667, 0.8234811943173409], [3.8731993994712823, 5.702363785147667, 0.8234811943173409]], [[3.873199399471282, 5.134198701739312, 1.3586930910348891], [4.401190314531325, 5.134198701739312, 1.3586930910348891], [4.401190314531325, 5.702930300474167, 1.3586930910348891], [3.873199399471282, 5.702930300474167, 1.3586930910348891], [3.873199399471282, 5.134198701739312, 1.3986151036024093], [4.401190314531325, 5.134198701739312, 1.3986151036024093], [4.401190314531325, 5.702930300474167, 1.3986151036024093], [3.873199399471282, 5.702930300474167, 1.3986151036024093]]] #FRIDGE
#all_boxes_range=[[[0.249, 0.499, 0.774], [1.751, 0.499, 0.774], [1.751, 1.501, 0.774], [0.249, 1.501, 0.774], [0.249, 0.499, 0.8260000000000001], [1.751, 0.499, 0.8260000000000001], [1.751, 1.501, 0.8260000000000001], [0.249, 1.501, 0.8260000000000001]], [[0.29899999999999993, 0.5489999999999999, -0.18600000000000005], [0.401, 0.5489999999999999, -0.18600000000000005], [0.401, 0.651, -0.18600000000000005], [0.29899999999999993, 0.651, -0.18600000000000005], [0.29899999999999993, 0.5489999999999999, 0.7659999999999999], [0.401, 0.5489999999999999, 0.7659999999999999], [0.401, 0.651, 0.7659999999999999], [0.29899999999999993, 0.651, 0.7659999999999999]], [[0.29899999999999993, 1.349, -0.18600000000000005], [0.401, 1.349, -0.18600000000000005], [0.401, 1.4509999999999998, -0.18600000000000005], [0.29899999999999993, 1.4509999999999998, -0.18600000000000005], [0.29899999999999993, 1.349, 0.7659999999999999], [0.401, 1.349, 0.7659999999999999], [0.401, 1.4509999999999998, 0.7659999999999999], [0.29899999999999993, 1.4509999999999998, 0.7659999999999999]], [[1.5989999999999998, 0.5489999999999999, -0.18600000000000005], [1.701, 0.5489999999999999, -0.18600000000000005], [1.701, 0.651, -0.18600000000000005], [1.5989999999999998, 0.651, -0.18600000000000005], [1.5989999999999998, 0.5489999999999999, 0.7659999999999999], [1.701, 0.5489999999999999, 0.7659999999999999], [1.701, 0.651, 0.7659999999999999], [1.5989999999999998, 0.651, 0.7659999999999999]], [[1.5989999999999998, 1.349, -0.18600000000000005], [1.701, 1.349, -0.18600000000000005], [1.701, 1.4509999999999998, -0.18600000000000005], [1.5989999999999998, 1.4509999999999998, -0.18600000000000005], [1.5989999999999998, 1.349, 0.7659999999999999], [1.701, 1.349, 0.7659999999999999], [1.701, 1.4509999999999998, 0.7659999999999999], [1.5989999999999998, 1.4509999999999998, 0.7659999999999999]]] #TABLE
#all_boxes_range=[[[3.801803249962627, 2.798124243974686, -0.050063745021820094], [4.398934257864952, 2.798124243974686, -0.050063745021820094], [4.398934257864952, 3.6138232537508013, -0.050063745021820094], [3.801803249962627, 3.6138232537508013, -0.050063745021820094], [3.801803249962627, 2.798124243974686, 0.7548704870939257], [4.398934257864952, 2.798124243974686, 0.7548704870939257], [4.398934257864952, 3.6138232537508013, 0.7548704870939257], [3.801803249962627, 3.6138232537508013, 0.7548704870939257]], [[3.217097979495048, 2.769108240962029, -0.050063745021820205], [3.570110748598099, 2.769108240962029, -0.050063745021820205], [3.570110748598099, 3.642838496804238, -0.050063745021820205], [3.217097979495048, 3.642838496804238, -0.050063745021820205], [3.217097979495048, 2.769108240962029, 0.7838857301473617], [3.570110748598099, 2.769108240962029, 0.7838857301473617], [3.570110748598099, 3.642838496804238, 0.7838857301473617], [3.217097979495048, 3.642838496804238, 0.7838857301473617]], [[3.5101837408633236, 3.226199499800802, 0.39260575091838834], [3.58548575181675, 3.226199499800802, 0.39260575091838834], [3.58548575181675, 3.544824745595456, 0.39260575091838834], [3.5101837408633236, 3.544824745595456, 0.39260575091838834], [3.5101837408633236, 3.226199499800802, 0.40060575091838835], [3.58548575181675, 3.226199499800802, 0.40060575091838835], [3.58548575181675, 3.544824745595456, 0.40060575091838835], [3.5101837408633236, 3.544824745595456, 0.40060575091838835]], [[3.5343434926958084, 2.8741577393412596, 0.39260575091838834], [3.57513200033617, 2.8741577393412596, 0.39260575091838834], [3.57513200033617, 3.2048625000191393, 0.39260575091838834], [3.5343434926958084, 3.2048625000191393, 0.39260575091838834], [3.5343434926958084, 2.8741577393412596, 0.40060575091838835], [3.57513200033617, 2.8741577393412596, 0.40060575091838835], [3.57513200033617, 3.2048625000191393, 0.40060575091838835], [3.5343434926958084, 3.2048625000191393, 0.40060575091838835]], [[3.1741110202760696, 2.8204960129261023, 0.5779345027208327], [3.2435712470502853, 2.8204960129261023, 0.5779345027208327], [3.2435712470502853, 3.587643731474877, 0.5779345027208327], [3.1741110202760696, 3.587643731474877, 0.5779345027208327], [3.1741110202760696, 2.8204960129261023, 0.6361732610464095], [3.2435712470502853, 2.8204960129261023, 0.6361732610464095], [3.2435712470502853, 3.587643731474877, 0.6361732610464095], [3.1741110202760696, 3.587643731474877, 0.6361732610464095]], [[3.2727112588377, 2.849713740408421, 0.3854447501748798], [3.8262027512134313, 2.849713740408421, 0.3854447501748798], [3.8262027512134313, 3.577601250350476, 0.3854447501748798], [3.2727112588377, 3.577601250350476, 0.3854447501748798], [3.2727112588377, 2.849713740408421, 0.6614444979429245], [3.8262027512134313, 2.849713740408421, 0.6614444979429245], [3.8262027512134313, 3.577601250350476, 0.6614444979429245], [3.2727112588377, 3.577601250350476, 0.6614444979429245]]]
#all_boxes_range=[[[3.1862777365475883, 5.069626060035825, 0.32445440387725766], [3.833652749660611, 5.069626060035825, 0.32445440387725766], [3.833652749660611, 5.10759665825665, 0.32445440387725766], [3.1862777365475883, 5.10759665825665, 0.32445440387725766], [3.1862777365475883, 5.069626060035825, 1.9208873894214626], [3.833652749660611, 5.069626060035825, 1.9208873894214626], [3.833652749660611, 5.10759665825665, 1.9208873894214626], [3.1862777365475883, 5.10759665825665, 1.9208873894214626]]]
all_boxes_range=[[[3.803266899943351, 5.094949591517448, 0.324454403877258], [3.8412374981641775, 5.094949591517448, 0.324454403877258], [3.8412374981641775, 5.74232460463047, 0.324454403877258], [3.803266899943351, 5.74232460463047, 0.324454403877258], [3.803266899943351, 5.094949591517448, 1.9208873894214626], [3.8412374981641775, 5.094949591517448, 1.9208873894214626], [3.8412374981641775, 5.74232460463047, 1.9208873894214626], [3.803266899943351, 5.74232460463047, 1.9208873894214626]]]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for box in all_boxes_range:
    edges = [
        [box[0], box[1], box[5], box[4]],
        [box[7], box[6], box[2], box[3]],
        [box[0], box[3], box[2], box[1]],
        [box[7], box[4], box[5], box[6]],
        [box[0], box[4], box[7], box[3]],
        [box[1], box[5], box[6], box[2]],
    ]
    ax.add_collection3d(Poly3DCollection(edges, alpha=.25, linewidths=1, edgecolors='r'))

# ax.scatter(4.2, 5.5, 0.85, color='green')
ax.set_xlim(2,8)
ax.set_ylim(2,8)
ax.set_zlim(0, 2)

plt.show()