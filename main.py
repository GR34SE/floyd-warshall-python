from prettytable import PrettyTable


# creates a matrix filled with 0's as placeholders for end results
def get_initial_results_list(number_of_vertices):
    return [[0] * number_of_vertices for _ in range(number_of_vertices)]


def get_results_matrix(vertices_entries):
    number_of_vertices = len(vertices_entries)
    results_matrix = get_initial_results_list(number_of_vertices)

    for i in range(number_of_vertices):
        for j in range(number_of_vertices):
            results_matrix[i][j] = vertices_entries[i][j]

    for k in range(number_of_vertices):
        for i in range(number_of_vertices):
            for j in range(number_of_vertices):
                if results_matrix[i][k] + results_matrix[k][j] < results_matrix[i][j]:
                    results_matrix[i][j] = results_matrix[i][k] + results_matrix[k][j]

    return results_matrix


if __name__ == '__main__':
    infinity = float("inf")

    # matrix representing distances between adjacent cities (vertices pairs)
    # infinity is used to represent the unknown distances on init
    # @see graph.png
    polish_major_cities_distances_matrix = [
        [0, 180, 140, 220, infinity, infinity, infinity],  # Poznań
        [180, 0, infinity, 220, infinity, infinity, 200],  # Wrocław
        [140, infinity, 0, 220, 300, infinity, infinity],  # Bydgoszcz
        [220, 220, 220, 0, 140, infinity, 200],  # Łódź
        [infinity, infinity, 300, 140, 0, 290, infinity],  # Warszawa
        [infinity, infinity, infinity, infinity, 290, 0, 80],  # Kraków
        [infinity, 200, infinity, 200, infinity, 80, 0]  # Katowice
    ]

    results = get_results_matrix(polish_major_cities_distances_matrix)

    polish_major_cities_labels = ["Poznań", "Wrocław", "Bydgoszcz", "Łódź", "Warszawa", "Kraków", "Katowice"]
    table = PrettyTable(["City:", *polish_major_cities_labels])

    for index in range(len(polish_major_cities_labels)):
        table.add_row([polish_major_cities_labels[index], *results[index]])

    print(table)
