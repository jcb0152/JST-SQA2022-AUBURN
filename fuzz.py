from TestOrchestrator4ML_main.label_perturbation_attack.knn import calculate_k, euc_dist, perform_inference, predict, calculate_metrics


if __name__ == "__main__":
    inputs = ["cars", 77, {"dictionary":"definition"}, 99, 0, "runner"]

    for x in inputs:
        try:
            euc_dist(x, "two")
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            predict(x, 47)
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            calculate_metrics(x, "input", 99)
        except Exception as e:
            print(e)
    
    for x in inputs:
        try:
            perform_inference(x, "two", 3, "four", 5)
        except Exception as e:
            print(e)

    for x in inputs:
        try:
            calculate_k(x, "second", "third", 4)
        except Exception as e:
            print(e)
