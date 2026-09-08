# Recursive \(F_\ell\) packets: path hitting, multiframe averaging, and the integral rounding barrier

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computer-assisted enumeration is used.

## 0. Verdict

Treat the recursive two-sided-rainbow factor \(F_\ell\) from
`ROTOR_SCD_PARITY_CHECK_CYCLE_TILING_20260725.md` as fixed.  The following
facts then hold.

1.  A lower target is not an abstract colour.  If the middle row is written
    as
    \[
      X_j=I_\pi(j,m),
    \]
    a rank-\((m-q)\) target \(T\) is represented exactly when a selected
    factor cycle contains a consecutive \((q+1)\)-vertex Johnson path in
    the up-set
    \[
      \mathcal U_T=\{X\in\tbinom{[n]}m:T\subseteq X\}.
    \]
    Its intersection is then \(T\).  In the odd attachment convention, an
    upper depth-\(q\) target is the complement of a lower depth-\((q-1)\)
    target.  This shift must be retained in every incidence count.

2.  Conjugating the nonlinear \(F_\ell\)-cycle atoms through all coordinate
    frames gives an **exact rational fractional** central-band SCD.  Every
    Boolean mask has weighted degree one, and the radius weights are exactly
    \[
      c_d=N_d-N_{d+1}\quad(d<H),\qquad c_H=N_H.
    \]
    This is fractional feasibility only.

3.  Whole nonlinear cycles are the correct physical unit for changing
    frames.  If \(H\ll\ell\ll m\), cutting each \(2\ell\)-cycle once costs
    \[
      O(HW/\ell)=o(W).
    \]
    Thus genuine cross-frame mixing is compatible with \(o(W)\) reset toll.

4.  A single fixed coordinate pairing still has a positive Gaussian
    pair-type capacity deficit.  The recursive order diversity inside
    \(F_\ell\) does not change this census.  A coefficient-one construction
    must mix coordinate matchings inside the selected integral object, not
    merely randomize or glue strata in one frame.

5.  Independent, maximum-entropy, or ordinary discrepancy rounding does
    not solve the integral problem.  At weighted degree one, independent
    rounding leaves \((e^{-1}+o(1))N_q\) holes and
    \((1/2+o(1))N_q\) colliding pairs in each diffuse rank.  Discrepancy
    estimates larger than one cannot imply exact Boolean ownership, because
    the rounded row sums are integers.  Conditioning only on exact middle
    ownership is also insufficient: a randomly relabelled one-frame factor
    is symmetric and exact in the middle while retaining the Gaussian
    capacity deficit.

Accordingly, no constant-one theorem is claimed.  The primary surviving
statement is the weaker direct-compiler gate \(\mathrm{MFUP}_A\): select an
integral, exact middle-owner partition, leave only \(o(W)\) aggregate
lower/upper path-hitting holes, and order the pieces with \(o(W)\) total
useful-prefix bridge excess.  An exact band SCD is a stronger sufficient
route, but it is not required by the literal compiler.

This note is a sufficient-construction analysis.  It does **not** assume or
claim that every near-optimal contiguous-OR word reduces to singleton
near-\(U\)-cycles, wreaths, or the atom system used here.

## 1. Exact attachment dictionary: ownership is path hitting

Let \(J(n,m)\) be the Johnson graph on \(\binom{[n]}m\).  For
\(T\in\binom{[n]}{m-q}\), write

\[
  \mathcal U_T=\{X\in\tbinom{[n]}m:T\subseteq X\}.
  \tag{1.1}
\]

### Lemma 1.1 (up-set path criterion)

Let

\[
 X_0,X_1,\ldots,X_q
 \tag{1.2}
\]

be a geodesic \(q\)-edge Johnson path: its successive moves delete \(q\)
distinct elements of \(X_0\).  Then, for
\(T\in\binom{[n]}{m-q}\),

\[
 \boxed{
 T=\bigcap_{i=0}^qX_i
 \quad\Longleftrightarrow\quad
 X_0,\ldots,X_q\in\mathcal U_T.}
 \tag{1.3}
\]

#### Proof

The forward implication is immediate.  Conversely, membership in
\(\mathcal U_T\) gives

\[
 T\subseteq\bigcap_{i=0}^qX_i.
\]

A geodesic \(q\)-edge Johnson path deletes \(q\) distinct elements of
\(X_0\), and none is restored along a shortest path.  Its common
intersection therefore has size \(m-q=|T|\).
Hence equality holds. \(\square\)

For a cyclic interval row, write exactly

\[
 X_j=I_\pi(j,m).
 \tag{1.4}
\]

Its consecutive windows are geodesic until the first coordinate return.
Therefore a rank-\((m-q)\) target is owned precisely by a consecutive
\((q+1)\)-vertex row path contained in \(\mathcal U_T\).  This is the
path-hitting formulation used below.

### Odd upper-depth convention

When \(n=2m+1\), a rank-\((m+q)\) upper target \(Y\) has complement

\[
 [n]\setminus Y\in\binom{[n]}{m+1-q}
   =\binom{[n]}{m-(q-1)}.
 \tag{1.5}
\]

Thus upper depth \(q\) is the complementary copy of lower depth \(q-1\),
with the corresponding cyclic index shift.  In particular, it is incorrect
to duplicate the lower depth-\(q\) equations and call them the odd upper
depth-\(q\) equations.  In even dimension \(n=2m\), complementation instead
pairs lower and upper targets at the same depth.

## 2. What the recursive factor supplies

Let \(\ell\) be a power of two and let \(F_\ell\) be the fixed neighbour
permutation of \(Q_\ell\).  Every cycle has length

\[
 R=2\ell,
 \tag{2.1}
\]

its transition word is \(\pi\pi\), and for every
\(q\le\ell/2\) its forward and backward labelled deletion maps are
injective.

Interpret the \(\ell\) cube coordinates as active split coordinate pairs.
For a cycle \(C\), a start \(x\in C\), and \(q\le\ell/2\), let

\[
 L_q^C(x)=\bigcap_{i=0}^qF_\ell^i(x),
 \qquad
 U_q^C(x)=\bigcup_{i=0}^qF_\ell^{-i}(x),
 \tag{2.2}
\]

after restoring the fixed full, empty, and inactive split coordinates.
Lemma 1.1 says that \(L_q^C(x)=T\) precisely when the corresponding
consecutive path lies in \(\mathcal U_T\).

For \(d\le H\le\ell/2\), define the packet

\[
 \mathcal A(C,d)
 =\bigsqcup_{x\in C}
 \bigl(
 L_d^C(x)\subset\cdots\subset L_1^C(x)\subset x
 \subset U_1^C(x)\subset\cdots\subset U_d^C(x)
 \bigr).
 \tag{2.3}
\]

The two-sided injectivity of \(F_\ell\) implies that (2.3) is a disjoint
union of \(R\) saturated radius-\(d\) chain segments.  In path language:
inside one atom no lower up-set, and no complementary upper up-set, is hit
twice at a certified depth.

This conclusion is **intra-atom**.  Different pair strata or different
coordinate frames can hit the same \(\mathcal U_T\).  Exact Boolean
ownership is precisely the demand that the integral selection choose one
of those hits, not zero or two.

## 3. Exact cross-frame fractional solution in path-hitting form

Use even central-band notation for the SCD ledger:

\[
 W=\binom{2m}m,
 \qquad
 N_q=\binom{2m}{m-q},
 \qquad
 \rho_q=N_q/W.
 \tag{3.1}
\]

For a band of depth \(H\), put

\[
 c_d=N_d-N_{d+1}\quad(0\le d<H),
 \qquad c_H=N_H,
 \tag{3.2}
\]

and

\[
 p_d=c_d/W.
 \tag{3.3}
\]

Then

\[
 \sum_{d=0}^Hp_d=1,
 \qquad
 \sum_{d=q}^Hp_d=\rho_q.
 \tag{3.4}
\]

Let \(\Omega_d\) be the multiset of all coordinate conjugates of one
radius-\(d\) nonlinear atom, with enough conjugates included to make the
family closed under the full coordinate permutation group.  Give every
member of \(\Omega_d\) the common weight

\[
 x_A=\frac{c_d}{R|\Omega_d|}.
 \tag{3.5}
\]

### Theorem 3.1 (exact fractional path-hitting ownership)

The weights (3.5) have the following exact properties.

1. Every middle owner has total weighted incidence one.
2. For every \(q\le H\) and every
   \(T\in\binom{[2m]}{m-q}\), the total weight of certified atom paths
   contained in \(\mathcal U_T\) is one.
3. The complementary upper target at the paired depth also has total
   weighted incidence one.
4. The weighted number of owners of exact radius \(d\) is \(c_d\).

#### Proof

Coordinate transitivity makes the weighted incidence constant on every
Boolean rank.  The total radius-\(d\) middle incidence is

\[
 |\Omega_d|\frac{c_d}{R|\Omega_d|}R=c_d.
\]

Summing over \(d\) gives \(W\), so every one of the \(W\) middle masks has
weight one.

At lower depth \(q\), a radius-\(d\) atom contributes exactly \(R\)
up-set path hits when \(d\ge q\), and none otherwise.  The total weighted
number of hits is

\[
 \sum_{d=q}^Hc_d=N_q.
 \tag{3.6}
\]

There are \(N_q\) possible targets, so transitivity gives weight one at
each \(T\).  Complementation proves the upper statement, with the shift in
(1.5) in the odd attachment convention.  The radius assertion was the
first calculation. \(\square\)

The theorem is exact over the full orbit.  A polynomial frame reservoir can
approximate these degrees arbitrarily accurately, but replacing (3.5) by
\(1+o(1)\) degrees does not settle the integral problem: the desired row
sums are the integer one.

The fractional number of atoms and the exact hard-prefix reset mass are

\[
 \sum_Ax_A=W/R,
 \tag{3.7}
\]

\[
 \widehat\Phi_{\rm frac}
 =2\sum_{d=0}^Hd\frac{c_d}{R}
 =\frac2R\sum_{q=1}^HN_q
 \le\frac{2HW}{R}.
 \tag{3.8}
\]

Thus \(H/\ell\to0\) gives fractional toll \(o(W)\).

### 3.2 The weaker direct-compiler fractional multicover

For \(\mathrm{MFUP}_A\), give every selected owner the full legal radius
\(H\); no SCD stopping-radius label is needed.  Let \(\Omega_H\) be the
coordinate orbit of radius-\(H\) atoms and give every atom the common weight

\[
 \beta=\frac{W}{R|\Omega_H|}.
 \tag{3.9}
\]

Every middle owner again has weighted degree one.  At lower depth \(q\),
the total number of weighted path hits is \(W\), so every target has exact
weighted hit load

\[
 \boxed{\mu_q=\frac{W}{N_q}=\rho_q^{-1}.}
 \tag{3.10}
\]

The complementary upper statement follows with the convention in (1.5).
The fractional hard-prefix toll remains at most

\[
 \frac{2HW}{R}=O(HW/\ell)=o(W).
 \tag{3.11}
\]

Thus the direct gate has more fractional shadow capacity than the SCD
system: its target load is \(\mu_q\ge1\), rather than exactly one.  The
integral problem is correspondingly weaker.  It still requires an exact
middle-owner partition and a common choice of physical pieces across all
depths.

## 4. Why a fixed frame is still impossible

Fix one perfect matching of the \(2m\) coordinates.  A middle owner of
pair type \(f\) has \(f\) full pairs, \(f\) empty pairs, and
\(m-2f\) split pairs.  The number of such owners is

\[
 V_f=\frac{m!}{f!^2(m-2f)!}2^{m-2f}.
 \tag{4.1}
\]

A rank-\((m-q)\) target of lower type \(f\) has \(f\) full pairs,
\(f+q\) empty pairs, and \(m-2f-q\) split pairs.  Their number is

\[
 T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
 \tag{4.2}
\]

Every pure fixed-frame up-set path starting at a type-\(f\) owner preserves
\(f\).  Hence, regardless of how the orientation cubes are tiled, the
number of distinct depth-\(q\) targets that can be hit is at most

\[
 \sum_f\min(V_f,T_{f,q}).
 \]

The forced deficit is therefore

\[
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
 \tag{4.3}
\]

For \(q=x\sqrt m+o(\sqrt m)\), \(x>0\) fixed,

\[
 \frac{D_{m,q}}W
 \longrightarrow
 \delta(x)
 :=e^{-x^2}\Phi_{\rm G}(x/2)-\Phi_{\rm G}(-3x/2)>0.
 \tag{4.4}
\]

This is the fixed-pair Gaussian capacity theorem proved in
`FIXED_PAIR_RESIDUAL_SCD.md`, `CUBE_SHADOW_TILING.md`, and the companion
pair-stratum census note.  The recursive \(F_\ell\) factor changes the order
field inside a source orientation cube; it does not change (4.1)--(4.3).

Consequently, the orbit average in Theorem 3.1 must be rounded to an object
which genuinely uses several coordinate matchings.  Choosing one frame and
only randomizing its intrastatum cycle factors cannot work.  Randomly
relabeling the entire one-frame factor also cannot work: that produces a
coordinate-symmetric distribution whose every realization still has the
deficit (4.4).

Whole \(F_\ell\)-cycles nevertheless make multiframe use physically cheap.
If the integral construction selects \(M\le W/R\) full atoms, cutting each
one once costs at most

\[
 \sum_{A\ {\rm selected}}2d(A)
 \le 2HM
 \le\frac{2HW}{R}
 =O(HW/\ell)=o(W).
 \tag{4.5}
\]

The number of main hard starts is \(O(W/\ell)=o(W/H)\), which is stronger
than merely \(o(W)\).  Frame changes are made between long packets; no
fresh \(\Theta(H)\) initialization is paid at each owner.

### Lemma 4.1 (whole-cycle interfaces are automatically sublinear)

Suppose \(M\) full legal \(F_\ell\)-cycles are pairwise disjoint on their
middle owners.  Suppose the remaining \(E\) middle owners are placed in at
most \(E\) nonempty legal residual pieces.  Then, in any order of all these
pieces,

\[
 \boxed{
 \sum_j(b_j-1)
 \le 2H(M+E)
 \le \frac{2HW}{R}+2HE.}
 \tag{4.6}
\]

Consequently, if \(H/\ell\to0\) and \(E=o(W/H)\), the total useful-prefix
bridge excess is \(o(W)\).

#### Proof

The exact useful-prefix bridge has

\[
 1\le b_j\le2H+1,
\]

because reverse-writing all \(2H+1\) useful blocks always initializes the
next piece.  Hence every bridge has excess at most \(2H\).  The \(M\) full
cycles contain \(MR\) distinct middle owners, so \(M\le W/R\).  There are
at most \(M+E-1\) bridges.  These observations give (4.6). \(\square\)

Thus, inside the whole-cycle rounding architecture, useful-prefix ordering
is not a separate asymptotic obstruction.  It becomes substantive only if
the integral rounding fragments a linear or \(W/H\)-scale number of cycles.
Every isolated middle owner admits a legal one-owner residual piece: choose
any \(H\) coordinates inside it and \(H\) outside it and reverse-write the
resulting useful prefix.  This observation pays the interface cost of a
small residual; it does not assert that those residual flags fill the
remaining shadow holes.

## 5. Independent probabilistic rounding has linear collision energy

Let \(\mathcal A\) be any finite atom multiset carrying an exact fractional
solution \(x_A\), and independently select atom \(A\) with probability
\(x_A\).  Fix one ownership row \(S\), and put

\[
 L_S=\sum_{A\ni S}Y_A,
 \qquad Y_A\sim\operatorname{Bernoulli}(x_A).
 \tag{5.1}
\]

Assume

\[
 \sum_{A\ni S}x_A=1,
 \qquad
 \eta=\max_Ax_A=o(1).
 \tag{5.2}
\]

### Proposition 5.1 (mean-one rounding barrier)

Uniformly in such rows,

\[
 \Pr(L_S=0)=e^{-1+O(\eta)},
 \tag{5.3}
\]

and

\[
 \mathbb E\binom{L_S}{2}
 =\frac12\left(1-\sum_{A\ni S}x_A^2\right)
 \ge\frac{1-\eta}{2}.
 \tag{5.4}
\]

#### Proof

By (5.2),

\[
 \log\Pr(L_S=0)
 =\sum_{A\ni S}\log(1-x_A)
 =-1+O\left(\sum_{A\ni S}x_A^2\right)
 =-1+O(\eta).
\]

Independence gives

\[
 \mathbb E\binom{L_S}{2}
 =\sum_{A<B\,:\,A,B\ni S}x_Ax_B
 =\frac12\left[\left(\sum_{A\ni S}x_A\right)^2
                 -\sum_{A\ni S}x_A^2\right],
\]

which is (5.4). \(\square\)

Summing (5.3)--(5.4) over one Gaussian target rank with
\(N_q=\Theta_A(W)\) gives

\[
 \mathbb E\#\{S:L_S=0\}
 =(e^{-1}+o(1))N_q=\Theta_A(W),
 \tag{5.5}
\]

\[
 \mathbb E\sum_S\binom{L_S}{2}
 \ge(1/2-o(1))N_q=\Theta_A(W).
 \tag{5.6}
\]

Thus independent rounding fails before reset accounting.  The
two-sided-rainbow property removes collisions *inside* one atom; (5.6)
counts collisions between different selected atoms.  A conditional-
expectation argument using only this first-moment estimate certifies at most
a linear collision-energy bound.  Reaching exact ownership requires
additional structure or strong negative dependence not present in the
product calculation.

The same observation applies to a maximum-entropy product distribution:
its one-row marginals solve the fractional equations but its typical output
is Poisson-like at mean one.

### Corollary 5.2 (independent rounding also misses the MFUP scale)

Apply the same calculation to (3.10).  If a target row has total fractional
load \(\mu_q=O(1)\) and maximum atom weight \(o(1)\), then

\[
 \Pr(L_T=0)=\exp(-\mu_q+o(1)).
 \tag{5.7}
\]

For every fixed sufficiently small \(\varepsilon>0\), uniformly over
\(1\le q\le\varepsilon\sqrt m\),

\[
 \mu_q=\exp(q^2/m+o(1))\le e^{\varepsilon^2+o(1)},
 \qquad N_q=\Theta_\varepsilon(W).
 \tag{5.8}
\]

Hence independent rounding has \(\Omega_\varepsilon(W)\) expected lower
holes at each of \(\Theta(\sqrt m)\) depths, and therefore
\[
 \mathbb E\sum_{q\le\varepsilon\sqrt m}M_q^-
   =\Omega_\varepsilon(W\sqrt m).
 \tag{5.9}
\]
The same applies to the complementary upper ledger.  This is far above the
\(o(W)\) aggregate defect allowed by \(\mathrm{MFUP}_A\).

## 6. What discrepancy would have to prove

For the stronger exact-SCD route, let \(A\) be the mask--atom incidence
matrix and let \(B\) record the radius counts.  The desired integral vector
\(y\) satisfies

\[
 Ay=\mathbf1,
 \qquad
 By=(c_0,\ldots,c_H),
 \qquad
 y\in\{0,1\}^{\mathcal A},
 \tag{6.1}
\]

up to explicitly listed residual atoms.  The vector \(x\) from Theorem 3.1
satisfies the real relaxation of (6.1).

Because \(Ay\) and \(By\) are integer vectors, an approximate discrepancy
bound proves (6.1) only if it is strictly smaller than one in every row:

\[
 \|A(y-x)\|_\infty<1
 \quad\Longrightarrow\quad
 Ay=\mathbf1,
 \tag{6.2}
\]

and similarly for \(B\), after the fractional right side is integral.
General vector-balancing bounds of order \(\sqrt r\), \(\sqrt{r\log n}\),
or even a fixed constant larger than one do not cross this integer gap.

An \(\ell^1\) discrepancy \(o(W)\) is enough for a literal OR repair only
when duplicate ownership is allowed and every omitted mask may be appended.
It is not an exact Boolean SCD: correct rank counts do not imply that the
residual masks are chain-decomposable.  In particular, flooring

\[
 \frac{c_d}{R}
 \tag{6.3}
\]

does not audit the radii.  Since a full atom has \(R=2\ell\) middle owners,
\(R\nmid c_d\) is typical.  The numerical remainder is at most \(R\) per
radius, but an exact proof must construct compatible residual chains; it
cannot replace that construction by the sentence “round the quotas.”

The mask--atom matrix is a multidimensional exact-cover matrix, not an
incidence matrix presently known to be totally unimodular.  Fractional
extreme points therefore cannot be assumed integral.

The direct \(\mathrm{MFUP}_A\) route relaxes the nonmiddle equations.  It
still requires exact middle rows, but for the lower/upper rows it asks only

\[
 \sum_{q\le H}\sum_T
 \mathbf1_{\{(Ay)_{q,T}=0\}}=o(W).
 \tag{6.4}
\]

Thus discrepancy is not ruled out in principle.  It must, however, give the
summed one-sided defect (6.4), not merely \(o(1)\) relative discrepancy
among the \(\Theta(W\sqrt m)\) shadow rows.  A uniform additive error
strictly below one would force every shadow load to be positive because
\(\mu_q\ge1\), but the standard bounds in this growing-column system are
much larger than one.  Any estimate which permits a positive fraction of
the rows to cross from load near one to load zero can still leave
\(\Theta(W\sqrt m)\) holes.
Moreover, (6.4) says nothing about the order of the selected pieces; the
useful-prefix bridge excess is a second, nonlinear scheduling statistic.

## 7. Entropy formulations and the missing negative dependence

For the stronger exact-SCD route, introduce one variable \(z_S\) for every
Boolean mask in the band and a radius marker \(u_d\).  For each
constant-radius atom \(A\), let \(M(A)\) be its mask set and \(d(A)\) its
radius.  Consider

\[
 P(\mathbf z,\mathbf u)
 =\prod_{A\in\mathcal A}
   \left(1+w_Au_{d(A)}^R\prod_{S\in M(A)}z_S\right).
 \tag{7.1}
\]

An exact all-atom band SCD with the prescribed radius counts would give a
positive coefficient

\[
 \left[
   \prod_{S\in\mathcal B_H}z_S
   \prod_{d=0}^Hu_d^{c_d}
 \right]P.
 \tag{7.2}
\]

Theorem 3.1 says that the logarithmic gradient equations associated with
(7.2) have an exact fractional solution.  It does **not** imply that the
coefficient (7.2) is positive.  Capacity-to-coefficient implications of
this kind require additional structure, such as stability or a proved
negative-dependence property.  No such property is established for (7.1).

Conditioning on exact middle ownership alone does not supply it.  A
distribution obtained by choosing one fixed-pair factor and then applying a
uniform global coordinate permutation has:

* exact middle ownership in every realization;
* full coordinate symmetry; and
* the correct average slot count in every target rank;

yet every realization inherits the positive fixed-frame deficit (4.4).
Thus symmetry, entropy, and first moments do not force path hitting.

A viable entropy proof would have to work on a measure already supported on
integral middle factors and prove **internal frame spread** together with a
coefficient or switching estimate strong enough to force every up-set row
sum to one.  That is substantially stronger than maximizing entropy subject
to the fractional marginals.

For \(\mathrm{MFUP}_A\), exact coefficient positivity is unnecessary.
Let \(\mathfrak F\) be the set of integral mixed-frame middle factors, and
for \(F\in\mathfrak F\) put

\[
 \mathcal H(F)=\sum_{q\le H}(M_q^-(F)+M_q^+(F)),
 \qquad
 \mathcal B(F)=\min_{\text{orders of }F}\sum_j(b_j-1).
 \tag{7.3}
\]

An entropy/Gibbs proof could instead establish

\[
 \min_{F\in\mathfrak F}\bigl(\mathcal H(F)+\mathcal B(F)\bigr)=o(W).
 \tag{7.4}
\]

The product measure in Section 5 is not supported on \(\mathfrak F\) and
has the wrong value of \(\mathcal H\).  Conditioning only on the middle
factor constraint need not repair it, by the one-frame counterexample.
What is missing is a switching or log-partition estimate which forces both
cross-frame path-hit spread and useful-prefix compatibility inside the same
integral factor.

For factors made from full \(F_\ell\)-cycles plus \(E=o(W/H)\) residual
owners, Lemma 4.1 already gives \(\mathcal B(F)=o(W)\), independently of
the ordering.  In that restricted class the entropy target reduces to

\[
 \min_{F\in\mathfrak F_{\rm full}}\mathcal H(F)=o(W).
 \tag{7.5}
\]

## 8. Exact radius audit for the stronger SCD output

This section concerns the stronger SCD route.  The direct compiler in
\(\mathrm{MFUP}_A\) uses radius-\(H\) legal pieces for all owners and does
not require the stopping-radius census below.

Suppose an integral selection of chain packets partitions the entire
central band.  Let \(a_d\) be the number of selected middle owners of
radius at least \(d\).  Every such owner contributes exactly one chain
member in rank \(m-d\), while no shorter chain does.  Exact Boolean
ownership therefore forces

\[
 a_d=N_d.
 \tag{8.1}
\]

Consequently the exact-radius counts are not optional side constraints:

\[
 a_d-a_{d+1}=N_d-N_{d+1}=c_d
 \quad(d<H),
 \qquad a_H=N_H.
 \tag{8.2}
\]

Conversely, correct aggregate values in (8.2) do not prove exact ownership;
the path-hitting equations at every \(T\) are still required.

For a radius-\(d\) rotor run containing \(t\) middle owners, the exact hard
prefix word length is

\[
 t+2d.
 \tag{8.3}
\]

If \(M\) full nonlinear cycles are selected and cut once each, their reset
toll is at most \(2HM\).  If an exceptional residual SCD is written as
rotor paths \(P\), its exact additional toll is

\[
 \Phi_{\rm exc}=\sum_{P}2d(P).
 \tag{8.4}
\]

Thus the completed band word has length

\[
 W+2HM+\Phi_{\rm exc}.
 \tag{8.5}
\]

For \(M\le W/R\), \(H/\ell\to0\), and
\(\Phi_{\rm exc}=o(W)\), this is \(W+o(W)\).  Merely knowing that the
residual contains \(o(W)\) masks is insufficient for (8.4): if each residual
owner is reset separately at radius \(H\), the cost is \(2H\) per owner.
The safe quantitative residual condition is a proved rotor-path toll
\(o(W)\), for example \(o(W/H)\) singleton residual owners.

## 9. The primary integral gate: direct useful-prefix compilation

For legal radius-\(H\) pieces, let \(b_j\) be the exact shortest positive
MTF bridge from the terminal last-occurrence state of piece \(j\) to the
useful ordered prefix of piece \(j+1\).  The direct compiler proved in
MATH_ATTACK_ORIENTATION_CUBE_DIRECT_LITERALIZATION_INTERFACE_TOLL_20260725.md
has exact length bound

\[
 W+2H+\sum_j(b_j-1)
 +\sum_{q=1}^H(M_q^-+M_q^+).
 \tag{9.1}
\]

The general direct-compiler target is therefore:

> **Mixed-frame useful-prefix necklace gate
> \(\mathrm{MFUP}_A\) — UNPROVED.**
> Let \(H=\lceil A\sqrt m\rceil\), and choose a power of two \(\ell\)
> with \(H=o(\ell)\) and \(\ell=o(m)\).  Select and order legal segments of
> coordinate-conjugated \(F_\ell\)-cycles such that:
>
> 1. their middle owners form an exact partition of the middle layer;
> 2. with lower holes tested by the up-set criterion (1.3), and upper holes
>    by the complementary convention (1.5),
>    \[
>      \sum_{q\le H}(M_q^-+M_q^+)=o(W);
>    \]
> 3. their exact useful-prefix bridges satisfy
>    \[
>      \sum_j(b_j-1)=o(W).
>    \]

By (9.1), \(\mathrm{MFUP}_A\) gives a literal central-band word of length
\(W+o(W)\).  Duplicate nonmiddle targets are harmless.  No common SCD
colour or exact stopping-radius count is required.

Lemma 4.1 gives a still cleaner sufficient form tailored to the recursive
factor:

> **Whole-cycle MFUP rounding gate — UNPROVED.**  Select
> coordinate-conjugated full \(F_\ell\)-cycles which are pairwise disjoint
> on their middle owners and cover all but \(E=o(W/H)\) middle owners.
> Put the residual owners into legal pieces, and require only
> \[
>   \sum_{q\le H}(M_q^-+M_q^+)=o(W).
> \]

The middle ownership is integral and exact after adding the residual
pieces.  Lemma 4.1 supplies the bridge clause of \(\mathrm{MFUP}_A\)
automatically.  This is the primary probabilistic/discrepancy rounding
target of the note.

### 9.1 Stronger optional gate: exact SCD selection

The exact-SCD target can also be stated without fractional language.

> **Integral multiframe \(F_\ell\) path-hitting gate
> \(\mathrm{IMF}_A\) — UNPROVED.**
> Let \(H=\lceil A\sqrt m\rceil\), and choose a power of two \(\ell\)
> with \(H=o(\ell)\) and \(\ell=o(m)\).  Select coordinate-conjugated
> nonlinear \(F_\ell\)-cycle atoms, together with an explicitly constructed
> residual rotor-path family, such that:
>
> 1. every middle mask has exactly one owner;
> 2. for every lower target \(T\) in the band, exactly one selected active
>    consecutive Johnson path lies in \(\mathcal U_T\);
> 3. the complementary upper equations hold, with the depth shift (1.5) in
>    the odd attachment convention;
> 4. the selected chains have the exact radius counts (8.2); and
> 5. the full-cycle cuts plus the residual rotor paths have total hard-prefix
>    toll \(o(W)\).

The output is integral by definition.  Items 1--4 say that it is one actual
central-band SCD, not separately balanced depthwise factors.  Item 5 is
automatic for the full atoms from \(H/\ell\to0\); its substantive residual
part is (8.4).  This stronger gate independently gives a \(W+o(W)\) band
word through the exact rotor--SCD compiler.  It is sufficient for the same
coefficient-one goal, but need not literally instantiate the radius-\(H\)
piece convention in \(\mathrm{MFUP}_A\).

The standard band-extension theorem then extends the band SCD to a full
Boolean SCD without altering its band rotor paths.  The audited outer-tail
word and the usual dimension transfer would give coefficient one if
\(\mathrm{IMF}_A\) held for every fixed \(A\).

## 10. What a successful probabilistic/discrepancy proof must add

The preceding audit rules out only generic rounding, not every correlated
construction.  A successful argument could take one of the following
ownership-first forms.

1. **Alternating multiframe trades.**  Start with an exact integral middle
   factor and use alternating exchanges among whole \(F_\ell\)-cycles.
   Every trade must preserve all middle owners while decreasing aggregate
   path-hit holes and keeping useful prefixes schedulable.  A batch trade,
   not a one-collision alteration, is needed to beat (5.9).  If the stronger
   SCD route is used, the same trades must also preserve all radius counts.

2. **A negatively dependent exact-factor measure.**  Construct a measure
   supported on integral mixed-frame middle factors and prove
   \(\mathcal H(F)=o(W)\) for a full-cycle output with a small residual;
   Lemma 4.1 then pays \(\mathcal B(F)\).  For fragmented outputs the bridge
   term must be restored.  For the stronger SCD route, this may instead be
   replaced by a positive lower bound for the exact coefficient (7.2).
   Coordinate symmetry and correct first moments alone are insufficient.

3. **A reservoir-adapted SCD absorber.**  Round to disjoint nonlinear atoms
   while reserving a structured set of owners whose unused masks are already
   known to admit an SCD and whose rotor-path toll is \(o(W)\).  A mere
   \(o(W)\) rank histogram is not such an absorber.

At present none of these three statements is proved.  The exact positive
advance is that the recursive \(F_\ell\) factor removes every intrapacket
rainbow and residence obstruction, full coordinate conjugacy removes the
fixed-frame deficit fractionally, and whole-cycle frame mixing has the
correct \(o(W)\) reset scale.  The unresolved obstruction is precisely the
integral cross-stratum path-hitting problem for an exact middle factor.
Useful-prefix scheduling is already settled for whole-cycle outputs with a
small residual.

## 11. Rounding checklist

For later use, an argument in this lane is incomplete if any of the
following steps is omitted.

1. **Middle integrality:** every middle mask must have one integral owner.
2. **Path legality:** a lower occurrence is credited only from a consecutive
   geodesic path contained in \(\mathcal U_T\).
3. **Upper indexing:** in the odd attachment, upper depth \(q\) is the
   complement of lower depth \(q-1\), not lower depth \(q\).
4. **Cross-frame use:** one fixed coordinate matching has deficit (4.4),
   even with the recursive \(F_\ell\) factor.
5. **Common selection:** the same integral pieces must control every depth
   and both signs.
6. **Radius scope:** \(\mathrm{MFUP}_A\) does not need stopping-radius
   counts; if the stronger SCD route is claimed, floors and remainders in
   \(c_d/R\) require an actual residual SCD.
7. **Collision accounting:** mean-one independent rounding has the linear
   losses (5.5)--(5.6).
8. **Discrepancy threshold:** exact middle rows require an error below one;
   shadow rows require total one-sided hole defect \(o(W)\), not merely
   small relative discrepancy.
9. **Interface weights:** for the direct compiler charge the exact
   \(\sum(b_j-1)\).  Lemma 4.1 makes it \(o(W)\) only when whole cycles and
   an \(o(W/H)\) residual are retained.  For independent hard starts charge
   \(2d\), not one.
10. **No converse assumption:** the packet construction is a sufficient
    route only; no reduction of arbitrary near-optimal OR words to
    near-\(U\)-cycles is used.

Subject to this checklist, all fractional, capacity, and reset calculations
above are exact.  The statements marked unproved are the primary
\(\mathrm{MFUP}_A\) gate and its stronger exact-SCD variant.
