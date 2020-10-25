from SetSimilaritySearch import all_pairs


def mapster(columns_list, similarity_func_name="jaccard", threshold=0.5, ignore_case=False):
    """
    Utility to cluster different datasets based on their columns
    :param columns_list:
    :param similarity_func_name: the name of the similarity function used;
        this function currently supports `"jaccard"` and `"cosine"`.
    :param threshold: the threshold used, must be a float between 0 and 1.0.
    :param ignore_case: ignore case in columns names
    :return:
    """
    if ignore_case:
        columns_list = [[col.lower() if isinstance(col, str) else col for col in cols] for cols in columns_list]
    pairs = all_pairs(columns_list, similarity_func_name=similarity_func_name, similarity_threshold=threshold)
    metadata_clusters = [{pair[0], pair[1]} for pair in pairs] + [{i} for i in range(len(columns_list))]

    metadata_final_clusters = []
    for cluster in metadata_clusters:
        i, n = 0, len(metadata_final_clusters)
        while i < n:
            if cluster & metadata_final_clusters[i]:
                cluster.update(metadata_final_clusters[i])
                del metadata_final_clusters[i]
                n -= 1
            else:
                i += 1
        metadata_final_clusters.append(cluster)

    return [__get_summary(columns_list, idx_set) for idx_set in metadata_final_clusters]


def __get_summary(columns_list, idx_set):
    columns_list = [columns_list[e] for e in idx_set]
    common_list = set(columns_list[0])
    all_list = set()
    for cols in columns_list:
        common_list = common_list & set(cols)
        all_list = all_list | set(cols)
    return {'idx': idx_set, 'common_columns': list(common_list), 'other_columns': list(all_list - common_list)}


if __name__ == '__main__':
    cols1 = ['col1', 'id', 'col2']
    cols2 = ['col1', 'id']
    cols3 = ['col3', 'idx', 'col2']
    cols4 = ['col4', 'idr']

    result = mapster([cols1, cols2, cols3, cols4])
    print(result)
