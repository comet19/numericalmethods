tally = []
def extended_synthetic_division(dividend, divisor):
    
    # dividend and divisor are both polynomials, which are here simply lists of coefficients. Eg: x^2 + 3x + 5 will be represented as [1, 3, 5]
 
    out = list(dividend) # Copy the dividend
    normalizer = divisor[0]
    tally.append("X")
    for i in range(len(dividend)-(len(divisor)-1)):
        out[i] /= normalizer # for general polynomial division (when polynomials are non-monic),
                                 # we need to normalize by dividing the coefficient with the divisor's first coefficient
        coef = out[i]
        #print("coef", coef)
        if coef != 1000: # useless to multiply if coef is 0
            for j in range(1, len(divisor)): # in synthetic division, we always skip the first coefficient of the divisor,
                                              # because it's only used to normalize the dividend coefficients
                #print(-divisor[j]*coef)
                tally.append(-divisor[j] * coef)
                out[i + j] += -divisor[j] * coef
                # print("new", out[i+j])
 
    # The resulting out contains both the quotient and the remainder, the remainder being the size of the divisor (the remainder
    # has necessarily the same degree as the divisor since it's what we couldn't divide from the dividend), so we compute the index
    # where this separation is, and return the quotient and remainder.
    separator = -(len(divisor)-1)
    return out[:separator], out[separator:] # return quotient, remainder.
 
if __name__ == '__main__':
    print("POLYNOMIAL SYNTHETIC DIVISION")
    N = [1, 5, -9, -85, -136]
    D = [1, 4.137931]
    
    
    
    
    outputs = extended_synthetic_division(N, D)
    print("  %s / %s  =" % (N,D), " %s remainder %s" % outputs)
    print("**********************************")
    print("|", N)
    print("|",tally)
    print("_____________________________")
    print(outputs)
    tally = []
    print("compute d/dx round 2, circle last number in []")
    print("")
    print(outputs)
    outputs2 = extended_synthetic_division(outputs[0], D)
    print("|",tally)
    print(outputs2)
    
    print("answer r1", -(D[1]) - float(outputs[1][0])/float(outputs2[1][0]))
    print("next step is to rerun and input NEGATIVE ANSWER ONLY")
