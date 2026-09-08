# Corner period bound and exponential native collar overhead

2026-09-08. Root's independent symbolic audit of the new user claim.
This note assumes the exact translated-return/denominator formula now
being audited separately. It uses no asymptotic probabilistic estimate
and no numerical experiment. Internal review is not external or formal
certification of the finite PBBS inputs.

## 1. Clear the period denominators using only profile corners

Let the positive, nonincreasing peak counts m_0,...,m_(h-1) partition r,
with n_s=1+2*sum_(t>=s)m_t, n_0=n=2r+1, n_h=1. On a maximal constant
block [b_(j-1),b_j), write m_s=a and x_(j-1)=n_(b_(j-1)),x_j=n_(b_j).
The circumference decreases by2a at each step. Hence, exactly,

    1/(n_s*n_(s+1))=(1/n_(s+1)-1/n_s)/(2a),
    sigma_(b_j)-sigma_(b_(j-1))
       =(b_j-b_(j-1))/(x_(j-1)*x_j).

Put D=lcm_j(x_(j-1)*x_j). Every boundary sigma_(b_j) has denominator
dividing D, including the initial sigma_0=0. At a strict interior t of
one block, m_(t-1)=m_t, so the incoming gap row t-1 has total zero.
Its least period is1 and repetition factor e_(t-1)=n_t. Telescoping gives

    e_(t-1)*sigma_t
       =n_t*sigma_(b_(j-1))+(t-b_(j-1))/x_(j-1).

The denominator on the right also divides D. At a boundary the relevant
e is an integer, so its multiplication cannot introduce any denominator.
Consequently every denominator in

    v=lcm_(1<=t<=h) den(e_(t-1)*sigma_t)

divides D, and therefore v|D. This argument includes the last block and
the one-site endpoint. It does not assume any row is primitive.

Every adjacent boundary product divides P=product_(j=0)^q x_j. Thus
D|P; pairwise coprimality is unnecessary. Since x_q=1 and the other q
factors are at most n, v<=n^q.

## 2. A lower bound on the actual word's overhead

There are q distinct positive peak counts, each represented at least
once, so r>=1+...+q=q(q+1)/2. Thus

    q<=Q_n=floor((sqrt(4n-3)-1)/2), 1<=q<=h.

For every native state,

    (2h-1)/v >=(2q-1)/n^q >=(2Q_n-1)/n^Q_n.

The second inequality holds because the ratio of successive terms is
(2q+1)/(n*(2q-1))<=1 for n>=3,q>=1. There is no hidden independence
or averaging-by-cycles assumption. The construction's exact state-average
identity gives

    C_n=N_n-W(n)
       >=ceil((2Q_n-1)*W(n)/n^Q_n).

Since Q_n<sqrt(n) and log W(n)=n*log2-O(log n), this proves

    C_n>=exp(n*log2-O(sqrt(n)*log n)).

The known endpoint lower-bound excess is only B(n)-W(n)=O(sqrt(n)).
Therefore the unchanged word N_n is strictly longer than B(n) for all
sufficiently large odd n. Better estimates of that SAME word's periods
cannot establish exact attainment. The even doubling of this unchanged
word retains exponential additive overhead as well.

## 3. Scope

This is a lower bound for C_n of the fixed native height-adaptive word,
not for nu(n)-W(n) or nu(n)-B(n). Changing the words, shortening collars,
recoding states, changing target assignments, or using other constructions
remains possible. The already verified shortened17word is such a distinct
finite construction; its24658upper bound is not contradicted.

The independent translated-return audit and exact finite census should
be read together with this note before promoting the new period formula
to the master handoff.
