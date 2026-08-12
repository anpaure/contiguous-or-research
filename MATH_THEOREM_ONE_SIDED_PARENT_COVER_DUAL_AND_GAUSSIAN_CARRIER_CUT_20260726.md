# The exact one-sided parent-cover dual and a Gaussian carrier cut for the canonical linear mixer

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let

\[
 \Omega=\binom{[2m]}m,\qquad W=|\Omega|,
 \qquad {\cal T}_q=\binom{[2m]}{m-q},\qquad N_q=|{\cal T}_q|.
\]

The exact residual after the linear-scale diverse compiler is not a
collision energy.  It is a partitioned maximum-cover problem.  This note
does three things.

1.  It formulates the all-depth, cross-parent target-support hypergraph
    and gives its exact LP/Hall dual.
2.  It gives a deterministic integral rounding theorem tailored to the
    one-sided objective.  If fractional parent laws have product-hole
    functional \(o(W)\), sequential conditional expectation chooses one
    legal state per parent with summed missing shadow \(o(W)\).  No
    floor/ceiling balance and no CPCR estimate is used.
3.  It exhibits an explicit dual cut for the **canonical** linear mixer
    in which every good cell uses its first \(16R\) flexible axes.  Apart
    from \(o(W/H)\) owners, those axes lie in a fixed carrier containing
    at most \((1/2+o(1))2m\) physical coordinates.  A Gaussian exterior-
    profile cut at any depth

    \[
                              q=A\sqrt m+O(1)                 \tag{0.1}
    \]

    has deficit \(\Omega_A(W)\).  Therefore the canonical parent atlas,
    even with arbitrary compiler orders and affine conjugates inside its
    installed packets, cannot satisfy

    \[
                              \sum_{q\le H}M_q=o(W)           \tag{0.2}
    \]

    whenever \(H\ge A\sqrt m\).

The obstruction is not the old fixed-quartet type cut.  It is a
macroscopic carrier cut created by the rule “take the first \(16R\)
flexible axes.”  A positive construction must export active directions
outside every fixed proper carrier on positive owner mass; merely changing
the cyclic order on the already selected axes cannot do so.

## 1. Legal parent states and the target-support hypergraph

Let \({\cal C}\) be the good parent product cells of the linear mixer.
Their owner sets are disjoint and

\[
                         G:=\sum_{C\in{\cal C}}|C|
                           =W-o(W/H).                         \tag{1.1}
\]

For a parent \(C\), let \(\Xi_C\) be its finite set of legal complete
states.  A state records, simultaneously for all packets of \(C\), all
allowed diverse-compiler orders, affine conjugates, and other choices
which leave the installed packet partition intact.  The same state must
be used at every protected depth.  Write

\[
 I_{C,q}(\xi)=\{L_q^\xi(X):X\in C\}\subseteq {\cal T}_q.
                                                                    \tag{1.2}
\]

Parent-cell literal recovery gives

\[
                              |I_{C,q}(\xi)|=|C|              \tag{1.3}
\]

for every \(C,q,\xi\).  It also gives the exact laminar maps between
these images, but no laminar map is imposed between distinct parents.

Use the typed target universe

\[
       {\cal T}^{\le H}:=\mathop{\dot\bigcup}_{q=1}^H
                    (\{q\}\times{\cal T}_q).                 \tag{1.4}
\]

The all-depth hyperedge belonging to state \(\xi\in\Xi_C\) is

\[
       E(C,\xi):=\mathop{\dot\bigcup}_{q=1}^H
                    (\{q\}\times I_{C,q}(\xi)).              \tag{1.5}
\]

Thus the hypergraph has one colour class \(\{E(C,\xi):\xi\in\Xi_C\}\)
per parent, and a legal factor chooses exactly one edge from every colour
class.  If \(\xi_C\) is the chosen state, put

\[
 \mu_q(T)=\sum_{C\in{\cal C}}{\bf1}_{T\in I_{C,q}(\xi_C)},
 \qquad
 M_q=|\{T\in{\cal T}_q:\mu_q(T)=0\}|.                         \tag{1.6}
\]

This is the promised cross-parent target-support hypergraph.  Its
objective is exactly \(\sum_qM_q\), not a surrogate quadratic energy.
If a legal trade couples a bounded or growing disjoint bundle of parent
cells, replace that bundle by one super-parent and let its states be the
legal joint states.  All statements below remain valid verbatim.  Thus
the formulation does not assume that a genuine cross-parent trade
factorizes into independent cell choices; it assumes only an
owner-disjoint partition into choice blocks.

## 2. Exact integer program and exact Hall dual

Introduce \(x_{C,\xi}\in\{0,1\}\) and a hole variable
\(z_t\in\{0,1\}\) for every typed target \(t\).  The exact minimum number
of missing lower shadows is

\[
 \begin{array}{ll}
 \text{minimize}&\displaystyle\sum_{t\in{\cal T}^{\le H}}z_t,\\[2mm]
 \text{subject to}
   &\displaystyle\sum_{\xi\in\Xi_C}x_{C,\xi}=1
                        \quad(C\in{\cal C}),\\[2mm]
   &\displaystyle z_t+\sum_{C,\xi:t\in E(C,\xi)}x_{C,\xi}\ge1
                        \quad(t\in{\cal T}^{\le H}).
 \end{array}                                                   \tag{2.1}
\]

Relax \(x,z\) to be nonnegative, with \(z_t\le1\).  The upper bound on
\(z_t\) is harmless at an optimum.  Linear-programming duality gives the
following exact formula.

### Theorem 2.1 (weighted one-sided Hall dual)

The fractional optimum of (2.1) is

\[
 \boxed{
 \operatorname {Hole}_{\rm LP}
   =\max_{0\le y_t\le1}
       \left\{
       \sum_{t\in{\cal T}^{\le H}}y_t
       -\sum_{C\in{\cal C}}
          \max_{\xi\in\Xi_C}\sum_{t\in E(C,\xi)}y_t
       \right\}.}                                             \tag{2.2}
\]

Consequently a fractional cover with at most \(E_0\) holes exists if and
only if, for every weight vector \(0\le y\le1\),

\[
 \sum_C\max_{\xi\in\Xi_C}y(E(C,\xi))
                       \ge \sum_ty_t-E_0.                     \tag{2.3}
\]

In particular an indicator \(y={\bf1}_A\) supplies the literal cut

\[
 |A|-\sum_C\max_{\xi\in\Xi_C}|A\cap E(C,\xi)|.               \tag{2.4}
\]

#### Proof

For fixed \(x\), minimizing in \(z_t\) gives

\[
 \max\left(0,1-\sum_{C,\xi:t\in E(C,\xi)}x_{C,\xi}\right).
\]

Use \(\max(0,1-a)=\max_{0\le y\le1}y(1-a)\), interchange min
and max in the finite LP, and minimize separately over the simplex
\(\{x_{C,\xi}\ge0:\sum_\xi x_{C,\xi}=1\}\).  Its minimum is the
negative of the largest state weight in that parent.  This is (2.2).
\(\square\)

The maximum in (2.2) is taken **after summing all depths**.  Thus this
dual enforces the common all-depth state and does not incorrectly solve
the depths independently.

## 3. Exact integral rounding for the missing-only objective

There is a useful integral theorem which requires neither total
unimodularity nor balanced target multiplicities.

Let \(x_C=(x_{C,\xi})_{\xi\in\Xi_C}\) be an arbitrary probability law
on the legal states of parent \(C\), and put

\[
 p_C(t)=\sum_{\xi:t\in E(C,\xi)}x_{C,\xi}.                    \tag{3.1}
\]

Define its product-hole functional by

\[
 \Phi(x)=\sum_{t\in{\cal T}^{\le H}}
                       \prod_{C\in{\cal C}}(1-p_C(t)).        \tag{3.2}
\]

### Theorem 3.1 (conditional-expectation parent rounding)

There is an integral choice \(\xi_C\in\Xi_C\) satisfying

\[
                              \sum_{q\le H}M_q\le\Phi(x).     \tag{3.3}
\]

Moreover it can be obtained by exposing the parents one at a time and,
at each exposure, choosing a state which does not increase the exact
conditional expectation of the number of holes.

#### Proof

Choose the parent states independently according to the laws \(x_C\).
A typed target \(t\) is missed with probability
\(\prod_C(1-p_C(t))\).  Summing over \(t\) proves that the expected
number of holes is exactly \(\Phi(x)\).  Hence one integral outcome has
at most this many holes.  For the deterministic version, after any
partial exposure the current conditional expectation is the average,
over the next parent's possible states, of the subsequent conditional
expectations.  Choose a state no larger than that average and continue.
\(\square\)

Thus a delocalized atlas would be complete if one constructed parent
laws with

\[
                              \Phi(x)=o(W).                    \tag{3.4}
\]

This is a genuine integral sufficiency theorem for the exact residual.
It is stronger than merely satisfying the fractional Hall inequalities,
but it is strictly weaker than controlling collision excess or CPCR.
It also makes the known polarization issue transparent: diffuse laws
with bounded Gaussian total intensity leave a positive product-hole
mass, whereas a near-deterministic home parent makes the corresponding
factor in (3.2) small.

## 4. The canonical first-axis rule has a fixed macroscopic carrier

We now specialize to the installed linear mixer.  Recall that its
complete macroblocks have \(2d\) physical coordinates and \(d\) matching
edges.  In a uniformly random Boolean owner, the number of singleton
matching edges in each macroblock is \(\operatorname {Bin}(d,1/2)\),
independently across complete macroblocks.

Fix

\[
 \varepsilon=m^{-1/8},\qquad
 L=\left\lceil{32R(1+\varepsilon)\over d}\right\rceil,        \tag{4.1}
\]

and let \(E\) be the union of the first \(L\) complete macroblocks in
the physical ordering.  Put \(e=|E|=2dL\) and \(F=[2m]\setminus E\).
Since \(m/128<R\le m/64\) and \(d=o(m)\),

\[
 {1\over4}+o(1)\le {e\over2m}\le {1\over2}+o(1).              \tag{4.2}
\]

Let \(Y_E\) be the number of flexible axes in these \(L\) macroblocks.
Under the unconditioned Boolean law,

\[
                 Y_E\sim\operatorname {Bin}(dL,1/2),
 \qquad {\bf E}Y_E\ge16R(1+\varepsilon).                     \tag{4.3}
\]

A Chernoff bound therefore gives

\[
 \Pr(Y_E<16R)\le \exp(-c\varepsilon^2R)
                         =\exp(-\Omega(m^{3/4})).              \tag{4.4}
\]

Conditioning on middle rank costs only \(O(\sqrt m)\), so the number of
middle owners in cells with \(Y_E<16R\) is

\[
                         e^{-\Omega(m^{3/4})}W=o(W/H).         \tag{4.5}
\]

The value \(Y_E\) is constant throughout a product status cell.  Hence,
on every other cell, the canonical instruction “take the first \(16R\)
flexible axes” takes all installed packet directions from \(E\).
Changing a compiler order or applying an affine conjugate to those
directions does not alter their physical support.  Therefore every
lower trace emitted by such a state satisfies

\[
                         L_q^\xi(X)\cap F=X\cap F.             \tag{4.6}
\]

This conservation law is the required dual invariant.

## 5. Gaussian exterior-profile deficit

The next statement is independent of the compiler.

### Theorem 5.1 (proper-carrier Hall deficit)

Let \(E\subset[2m]\), \(e=|E|\), and suppose

\[
             \beta_m={e\over2m}\in[\beta_0,1-\beta_0]         \tag{5.1}
\]

for some fixed \(\beta_0>0\).  Suppose a family of injective maps from
middle owners to rank-\((m-q)\) targets preserves the exterior \(F\):

\[
                               T\cap F=X\cap F.                \tag{5.2}
\]

If \(q=A\sqrt m+O(1)\), \(A>0\) fixed, and at most \(B\) source
occurrences use maps which violate (5.2), then the number of uncovered
targets is at least

\[
                               c(A,\beta_0)W-B                \tag{5.3}
\]

for all sufficiently large \(m\).

#### Proof

For an exterior cardinality \(s\), the total numbers of middle sources
and lower targets are

\[
 V_s=\binom{|F|}{s}\binom e{m-s},\qquad
 T_s=\binom{|F|}{s}\binom e{m-q-s}.                           \tag{5.4}
\]

Because (5.2) forbids movement between exterior profiles and each source
has only one image, the conserving maps leave at least

\[
                               \sum_s(T_s-V_s)_+              \tag{5.5}
\]

targets uncovered before the \(B\) exceptional source occurrences are
used.  Each exceptional occurrence covers at most one further target,
so \(B\) is subtracted at the end.

Write \(e=2\beta_m m\), ignoring harmless integer errors, and choose

\[
 s=(1-\beta_m)(m-q)+z\sqrt m+O(1).                            \tag{5.6}
\]

If \(k=m-q-s\), then

\[
 k={e\over2}-(\beta_mA+z)\sqrt m+O(1),
 \qquad
 k+q={e\over2}+((1-\beta_m)A-z)\sqrt m+O(1).                 \tag{5.7}
\]

Uniform central Stirling expansion gives

\[
 \begin{aligned}
 \log {V_s\over T_s}
 &=\log{\binom e{k+q}\over\binom e k}\\
 &=-{(1-2\beta_m)A^2-2Az\over\beta_m}+o(1).                 \tag{5.8}
 \end{aligned}
\]

Take \(z=-A\) and then a sufficiently small fixed interval around that
value.  Uniformly for \(\beta_m\in[\beta_0,1-\beta_0]\), (5.8) is at
most \(-c_1(A,\beta_0)<0\).  Thus on this interval

\[
                               V_s\le(1-c_2)T_s.              \tag{5.9}
\]

The hypergeometric local central limit theorem, uniformly on the same
compact beta interval, gives

\[
                    \sum_{s\text{ in the interval}}T_s
                                  \ge c_3N_q.                 \tag{5.10}
\]

Finally \(N_q/W\to e^{-A^2}\), so (5.5), (5.9), and (5.10), followed by
the preceding \(B\)-ledger, imply (5.3).  The use of the local limit
theorem can equivalently be replaced
by Stirling's formula summed over an interval of width
\(\Theta(\sqrt m)\). \(\square\)

The relevant Hall witness is literal.  Let \(J\) be the interval of
exterior sizes used above and set

\[
              A_J=\{(q,T):|T\cap F|\in J\}.                  \tag{5.11}
\]

For any parent state supported in \(E\), injectivity and (4.6) give

\[
 \max_{\xi\in\Xi_C}|A_J\cap E(C,\xi)|
     \le |\{X\in C:|X\cap F|\in J\}|.                         \tag{5.12}
\]

Summing (5.12) over the disjoint parent cells bounds the second term of
(2.4) by \(\sum_{s\in J}V_s\).  The first term is
\(\sum_{s\in J}T_s\).  Equations (5.9)--(5.10) therefore make
\(y={\bf1}_{A_J}\) an explicit \(\Omega_A(W)\) dual certificate.

## 6. Consequence for the linear-scale diverse compiler

Apply Theorem 5.1 to the carrier in Section 4.  Here
\(\beta_m\in[1/4+o(1),1/2+o(1)]\).  The exceptional cells in (4.5)
can cover at most \(o(W/H)\) further targets at one depth, and the
original bad-cell leave has the same negligible scale.  Hence for every
fixed \(A>0\) and every protected depth \(q=A\sqrt m+O(1)\),

\[
                M_q\ge c_AW-o(W)=\Omega_A(W).                 \tag{6.1}
\]

In particular, if \(H\ge A\sqrt m\), then

\[
                              \sum_{q\le H}M_q\ne o(W).       \tag{6.2}
\]

This proves a no-go for the canonical first-axis parent atlas at the LP
level, before any integral-rounding issue arises.  It does **not** rule
out the linear-scale compiler itself.  It identifies the exact repair
which any positive atlas must implement:

* on \(\Omega(W)\) owner mass, legal parent states must use physical
  directions outside the early carrier \(E\), or trade owners between
  parents in a way which changes \(X\cap F\) (Theorem 5.1 shows that
  \(o(W)\) such exports cannot repair the cut);
* these exports must occur in the common all-depth state, because the
  maximum in (2.2) couples all \(q\);
* once such a delocalized state library supplies laws satisfying
  \(\Phi=o(W)\), Theorem 3.1 performs the desired integral selection
  directly, without proving CPCR or floor/ceiling balance.

Thus the remaining constructive problem is narrower than CPM/CPCR:
build a genuinely delocalized cross-parent state library and prove its
product-hole bound.  Context-coded order changes inside a fixed carrier
cannot solve the summed missing-shadow gate.
