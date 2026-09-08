# Six-slot `h=5`: nested-ray transport and complete large-excess closure

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical sign theorem.  It reorganizes
the reflected `h=5` gate into three ordered compact transport rays and six
positive period gains.  A new two-sided two-fifths anchor makes the third
ray free, while the sharp global compact price bounds the first two losses.
The six period gains then prove every canonical inert `h=5` table positive
whenever its endpoint excess satisfies `delta>=A/15`.  The interval
`0<delta<A/15` remains open.  No search or sampled computation is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F(w)=F_A(w),
 \qquad
 C=F(0),
\tag{0.1}
\]

and retain

\[
 L={5503\over125000},
 \qquad
 G={533\over10000},
 \qquad
 V_5={4973\over100000},
 \qquad
 \varepsilon={1\over20000}.
\tag{0.2}
\]

The authenticated train facts are

\[
 C>L,
 \qquad
 F(w)>L\quad(0\le w\le A/4),
 \qquad
 F(w)<G\quad(0\le w\le A/2),
\tag{0.3}
\]

\[
 F(A/5)<V_5,
 \qquad
 F'(w)<0\quad(4A/25\le w\le A/2),
\tag{0.4}
\]

and

\[
 F(w)>0\quad(0\le w\le A/2),
 \qquad
 |F(w)+F(A-w)|<\varepsilon.
\tag{0.5}
\]

## 1. A two-sided two-fifths anchor

For `0<z<25`, write

\[
 U_{24}(z)=\sum_{j=0}^{23}{z^j\over j!}
 +{z^{24}\over24!(1-z/25)}.
\tag{1.1}
\]

Then `e^z<U_24(z)`.

### Lemma 1.1

\[
\boxed{
 {1\over100}<F(2A/5)<{107\over5000}<{11\over500}.}
\tag{1.2}
\]

#### Proof: upper bound

The first four adverse Gaussian exponents are

\[
 {9\pi\over100},
 \qquad {49\pi\over100},
 \qquad {36\pi\over25},
 \qquad {289\pi\over100}.
\tag{1.3}
\]

Using `pi<355/113`, direct positive-denominator substitution in (1.1)
gives the strict lower Gaussian bounds

\[
 {7535\over10000},
 \qquad {2143\over10000},
 \qquad {107\over10000},
 \qquad {1\over10000}.
\tag{1.4}
\]

Their sum is `9786/10000`.  Discarding the remaining adverse tail gives

\[
                         F(2A/5)<1-{9786\over10000}
                         ={107\over5000}.
\tag{1.5}
\]

#### Proof: lower bound

Using `pi>333/106`, finite positive exponential polynomials of degrees
`3,6,10,14` give respectively

\[
 e^{-9\pi/100}<{151\over200},
 \qquad
 e^{-49\pi/100}<{43\over200},
\tag{1.6}
\]

\[
 e^{-36\pi/25}<{11\over1000},
 \qquad
 e^{-289\pi/100}<{3\over25000}.
\tag{1.7}
\]

The first omitted adverse term has exponent \(121\pi/25\).  The degree-15
positive polynomial at `40293/2650` is greater than two million, so that
term is below `1/2000000`.  Every successive ratio is below `1/1000`:
the smallest exponent gap is \(49\pi/20\), and the degree-seven positive
polynomial at `16317/2120` exceeds one thousand.  Hence the complete
omitted tail is below `1/1000000`.

The full adverse bank is therefore smaller than

\[
 {151\over200}+{43\over200}+{11\over1000}
 +{3\over25000}+{1\over1000000}
 ={981121\over1000000}.
\tag{1.8}
\]

Thus

\[
 F(2A/5)>{18879\over1000000}>{1\over100}.
\]

This proves (1.2).  \(\square\)

## 2. The compact train is an ordered three-ray transport

Use the reflected physical coordinates from the preceding theorem:

\[
 (c_1,c_2,c_3,c_4,c_5)=(x,y,A-m,A-v,A-u),
\tag{2.1}
\]

with endpoint period `A+delta`.  The exact reflected decomposition is

\[
\begin{aligned}
 \mathscr E_5={}&C+D_\delta(0)
 +G_\delta(x,u)+G_\delta(y,v)+M_\delta(m)\\
 &+\Theta(u)+\Theta(v)+\Theta(m).
\end{aligned}
\tag{2.2}
\]

Collect the compact pieces as

\[
\boxed{
 T_5=C-F(u)+F(x)-F(v)+F(y)-F(m).}
\tag{2.3}
\]

The physical polytope gives

\[
\boxed{
 0\le u\le {A\over6},
 \qquad x\le v,
 \qquad y\le m,
 \qquad v\ge {A\over5},
 \qquad m\ge {2A\over5},}
\tag{2.4}
\]

as well as

\[
                         0\le x\le {A\over5},
 \qquad 0\le y\le {2A\over5}.
\tag{2.5}
\]

### Lemma 2.1 (first ray)

\[
                         C-F(u)>-{9276\over1000000}.
\tag{2.6}
\]

#### Proof

Equations (0.2)--(0.3) give

\[
 C-F(u)>L-G
 ={44024-53300\over1000000}
 =-{9276\over1000000}.
\]

\(\square\)

### Lemma 2.2 (second ray)

\[
                         F(x)-F(v)>-{5706\over1000000}.
\tag{2.7}
\]

#### Proof

If `x>=4A/25` and `v<=A/2`, decrease on the fixed threshold interval and
`x<=v` give `F(x)>=F(v)`.  If instead `v>A/2`, reflection gives

\[
 F(v)<\varepsilon<F(x),
\]

because `A-v<A/2` and `F(x)>L`.

Now suppose `x<4A/25`.  Then `F(x)>L`.  Since `v>=A/5`, decrease from
`4A/25` gives `F(v)<=F(A/5)<V_5` when `v<=A/2`; when `v>A/2`, reflection
again gives \(F(v)<\varepsilon<V_5\).  Hence

\[
 F(x)-F(v)>L-V_5
 ={44024-49730\over1000000}
 =-{5706\over1000000}.
\]

\(\square\)

### Lemma 2.3 (third ray)

\[
                         \boxed{F(y)-F(m)>0.}
\tag{2.8}
\]

#### Proof

If `y>=4A/25` and `m<=A/2`, decrease and `y<=m` give the result.  If
`m>A/2`, reflection gives \(F(m)<\varepsilon\), while monotonicity and Lemma 1.1
give

\[
 F(y)\ge F(2A/5)>{1\over100}>\varepsilon.
\]

If `y<4A/25`, then `F(y)>L`.  Since `m>=2A/5`, monotonicity and Lemma 1.1
give `F(m)<=F(2A/5)<11/500<L` when `m<=A/2`; when `m>A/2`, reflection
gives \(F(m)<\varepsilon<L\).  Every case is strict.  \(\square\)

### Corollary 2.4

\[
                         \boxed{T_5>-{14982\over1000000}.}
\tag{2.9}
\]

## 3. Six uniform period gains

The period gain

\[
 D_\delta(w)=F_{A+\delta}(w)-F_A(w)
\]

is decreasing in `w` on `[0,A]`.  Indeed, after the common compact term
cancels, its `q`-th summand is

\[
 e^{-(A+qA+w)^2}-e^{-(A+q(A+\delta)+w)^2}.
\tag{3.1}
\]

The function `s exp(-s^2)` is decreasing for `s>=2A`, so differentiating
(3.1) with respect to `w` gives a negative result.

The six gain arguments in (2.2) are

\[
                         0, x, A-u, y, A-v, A-m.
\]

The density rows give

\[
 x\le {A\over5},
 \quad y\le {2A\over5},
 \quad A-m\le {3A\over5},
 \quad A-v\le {4A\over5},
 \quad A-u\le A.
\tag{3.2}
\]

Consequently their total gain is at least

\[
\boxed{
 \mathcal P_5(\delta)
 :=\sum_{j=0}^{5}D_\delta(jA/5).}
\tag{3.3}
\]

Combining (2.2), Corollary 2.4, and the three theta bounds gives the
one-dimensional lower gate

\[
\boxed{
 \Phi>\mathcal P_5(\delta)-{15132\over1000000}.}
\tag{3.4}
\]

## 4. Signing the large-excess interval

The function \(\mathcal P_5(\delta)\) increases with `delta`.  It therefore
suffices to price it at `delta=A/15`.

Retain only the `q=1` summand of every period gain.  Put

\[
                         t_j={31+3j\over15},
 \qquad 0\le j\le5.
\tag{4.1}
\]

Since `s exp(-s^2)` decreases beyond `2A`, integration over an interval
of length `A/15` gives

\[
 D_{A/15}(jA/5)
 >{\pi\over30}t_j e^{-\pi t_j^2/4}.
\tag{4.2}
\]

Using `pi<355/113`, direct `U_24` cross multiplication gives

\[
\begin{array}{c|cccccc}
j&0&1&2&3&4&5\\ \hline
e^{-\pi t_j^2/4}
&349/10000&176/10000&835/100000
&37/10000&155/100000&61/100000
\end{array}
\tag{4.3}
\]

as strict lower bounds.  Their weighted sum is

\[
 \sum_{j=0}^{5}t_j b_j={55799\over375000}.
\tag{4.4}
\]

Using `pi>333/106` in (4.2) therefore gives

\[
\boxed{
 \mathcal P_5(A/15)
 >{333\over3180}{55799\over375000}
 ={2064563\over132500000}.}
\tag{4.5}

The adverse constant in (3.4) is

\[
 {15132\over1000000}={3783\over250000}.
\tag{4.6}
\]

Subtracting (4.6) from (4.5) leaves

\[
                         {59573\over132500000}>0.
\tag{4.7}
\]

### Theorem 4.1 (complete large-excess `h=5` closure)

Every canonical inert size-five-efficient six-slot table with

\[
                         {A\over15}\le\delta<{A\over5}
\]

has strictly positive Bellman functional.  More precisely,

\[
                         \boxed{\Phi>{59573\over132500000}.}
\tag{4.8}
\]

## 5. Remaining chamber

The threshold face `delta=0` is already positive.  After Theorem 4.1, the
only unresolved part of the canonical inert `h=5` branch is

\[
                         \boxed{0<\delta<{A\over15}.}
\tag{5.1}
\]

Thus two thirds of the endpoint-excess interval, including all three
endpoint faces and their intersections, is closed by one uniform nested-ray
argument.  No face-by-face KKT analysis is needed there.

## 6. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| exact reflected `h=5` polytope and gate | `MATH_THEOREM_SIX_SLOT_H5_REFLECTED_THREE_RAY_SCALAR_GATE_20260804.md` | `2f26836e6c46974153136e45247ae10c3f5ff44a8bd9f55d60e511b98d091aef` |
| sharp global price, threshold monotonicity, and one-fifth anchor | `MATH_THEOREM_APERY_PERIOD25_SHARP_GLOBAL_PRICE_AND_THRESHOLD_RAY_COMPLETE_POSITIVITY_20260804.md` | `61265fdf0e355aae0c6c786f9725ee639a427a1efb866fa21191ccb7b575653a` |
| threshold floor, half-band positivity, and reflection | `MATH_THEOREM_SIX_SLOT_ENDPOINT_EFFICIENT_SUBCOMPLEMENTARY_PAIR_CLOSURE_20260804.md` | `4929d9e074816be68ece5a97203c5ea1696fd2f79f8445da9cc746ad205209e0` |
