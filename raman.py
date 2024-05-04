from RamanSpectrum_repository import RamanSpectrumProcessor

if __name__ == '__main__':
    processor = RamanSpectrumProcessor()
    key = ""
    while key != "q":
        print("Press p to proceed or press q to quit")
        img_name = input("Enter the name of the image file: <img_name>.png/.jpg/.bmp\n")
        processor.read_img(img_name)
        key = input("[Next: graph] Press p to proceed or press q to quit\n")
        graph_file_name = input("Enter the name of the graph file: ")
        if graph_file_name == "":
            img_name.split(".")[0]
            graph_file_name = f"{img_name.split('.')[0]}_graph.png"
        processor.get_spectrum_graph(graph_file_name)
        key = input("[Next: csv] Press p to proceed or press q to quit\n")
        csv_file_name = input("Enter the name of the csv file: ")
        if csv_file_name == "":
            csv_file_name = f"{img_name.split('.')[0]}.csv"
        processor.get_spectrum_csv(csv_file_name)
        key = input("[Next: csv] Press p to proceed or press q to quit\n")
        processor.outFigCSV()
        key = "q"