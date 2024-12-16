import numpy as np
import tabeline as tl
from abm import simulate

if __name__ == "__main__":
    result = simulate(
        models="TMDD.model",
        parameters="TMDD_parameters_orig.csv",
        times=[
            "1:min",
            "5:min",
            "10:min",
            "15:min",
            "30:min",
            "1:hr",
            "6:hr",
            "12:hr",
            "1:d",
            "2:d",
            "4:d",
            "5:d",
            "7:d",
            "10:d",
            "15:d",
            "20:d",
            "25:d",
        ],
        outputs=["L"],
    )
    result_tl = result.to_tabeline()
    print(result_tl)

    random_state = np.random.RandomState(0)
    error = 0.4
    data = np.exp(random_state.normal(np.log(result_tl[:, "L"]), error))
    data_25d_tl = tl.DataFrame(
        time=result_tl[:, "t"],
        time_unit="d",
        measurement=data,
        measurement_unit="nmol",
        output="L",
        exponential_error=error,
    )
    print(data_25d_tl)
    data_25d_tl.write_csv("TMDD_data_25d.csv")

    data_10d_tl = data_25d_tl.filter("time <= 7.0")
    data_10d_tl.write_csv("TMDD_data_7d.csv")
