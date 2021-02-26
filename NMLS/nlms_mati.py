def nmls_mati(x,p,u):
    # x - input signal
    # p - number of taps
    # u - learning rate

    #zamienic d z x
    import numpy as np
    n = len(x)
    h = np.zeros(p-1) #init filter
    d = np.ones(n) # signal which will be imitating input signal
    y_approx = [] #creating variables

    for i in range(n):
        if i >= p - 1:
            temp = h
            ref_signal = d[i - p + 1:i]  # to jest ten badany input
            multiplication = sum([ref_signal[j] * temp[j] for j in range(p - 1)])

            error_output = x[i] - multiplication
            normalization = sum([ref_signal[j] ** 2 for j in range(p - 1)])
            h = temp + np.multiply(ref_signal, u * error_output) / normalization

            y_approx.append(sum(h * ref_signal)) # multiplying given input by filter, appending to given signal
    return y_approx
