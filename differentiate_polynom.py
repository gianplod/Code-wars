def differentiate(equation, point):

    def separate_terms(equation):  # returns eq_terms
        j = 0
        eq_terms = []
        for i, char in enumerate(equation):

            if char == '-' and i == 0:
                pass
            elif char == '-' and i != 0:
                eq_terms.append(equation[j:i])
                j = i
            elif char == '+':
                eq_terms.append(equation[j:i])
                j = i+1
            elif i == len(equation)-1:
                eq_terms.append(equation[j:])
            else:
                continue
        return eq_terms

    def separate_exp(eq_terms):  # returns exp

        exp = []
        for term in eq_terms:
            if 'x' in term:
                if '^' in term:
                    exp.append(int(term[(term.index('^'))+1:]))
                else:
                    exp.append(1)
            else:
                exp.append(0)

        return exp

    def separate_coeff(eq_terms):  # returns coeff

        coeff = []
        for term in eq_terms:
            if 'x' not in term:
                coeff.append(int(term))

            else:
                if term[0] == 'x':
                    coeff.append(1)
                elif term[0] == '-' and term[1] == 'x':
                    coeff.append(-1)
                else:
                    coeff.append(int(term[0:term.index('x')]))

        return coeff

    def calculate_derivative(coeffs, exps, point):

        derivative_at_point = sum(
            [int(exps[i]*coeffs[i]*point**(exps[i]-1)) for i in range(len(exps))])

        return derivative_at_point

    return calculate_derivative(separate_coeff(separate_terms(equation)),
                                separate_exp(separate_terms(equation)), point)


differentiate("-5x^2+10x+4", 3)
