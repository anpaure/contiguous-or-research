# Outward-ray seam ports, acyclic SDRs, and lower-Hall separation

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: exact interface theorem.  Positive deadline slack does not absorb an
upper casualty which is absent from the owner interval tower.  The full
multi-seam upper condition is pointwise, not a unit-capacity matching.  In
the protected one-outgoing-seam architecture, a zero-cost repair is
equivalent to an acyclic system of distinct successor representatives, or
equivalently to a forward Hall condition.  The common lower compiler remains
a separate condition.

## 1. Setting and the explicit ray casualty lists

Let

\[
 r=\lceil k/2\rceil,
 \qquad W={k\choose r},
 \qquad \Lambda=\sum_{s=1}^{r-1}{k\choose s},
\]

and take the monotone-deadline parameters

\[
 d=\min\left\{j\ge0:jW+{j+1\choose2}\ge\Lambda\right\},
 \qquad B(k)=W+d.                                    \tag{1.0}
\]

and let a rank-`r` cycle factor be opened into pairwise vertex-disjoint
directed path fragments

\[
 P_a=(X_{a,0},X_{a,1},\ldots,X_{a,n_a-1}),
 \qquad 1\le a\le b.                                  \tag{1.1}
\]

Their vertices together are the complete rank-`r` layer.  Put

\[
 x_a=X_{a,n_a-1},\qquad
 V_a=\bigcup_{j=0}^{n_a-1}X_{a,j}.                    \tag{1.2}
\]

The cut and orientation are chosen so that the cut flank is the transition
from `x_a` to `X_(a,0)`.  Assume the fixed-width hypothesis `(FW)` and the
assigned-provider convention of Theorem 4.4 in
`MATH_THEOREM_R_PROTECTED_WEDGE_RAYS_AND_PRODUCT_SPILL_20260730.md`.
Let `R_a` be the set of upper targets assigned to component `a` which lose
all retained component-interior witnesses after the cut.  If `(E1)` protects
depth two, then

\[
 \mathcal R_a\subseteq
 \left\{x_a\cup X_{a,0}\cup\cdots\cup X_{a,q-1}:
                3\le q\le k-r\right\},               \tag{1.3}
\]

where only unions of rank exactly `r+q` can occur.  Consequently

\[
 |\mathcal R_a|\le\max\{k-r-2,0\},\qquad
 \left|\bigcup_a\mathcal R_a\right|
 \le b\max\{k-r-2,0\}.                               \tag{1.4}
\]

Repeated target masks across components are counted only once in the second
quantity.  All results below remain true for any explicitly supplied lists
`R_a`; (1.3)--(1.4) are the protected-ray specialization.

## 2. Exact upper projection: lower slack is not an upper port

Let `d>=0`, let `T=(T_0,...,T_(W-1))` be a permutation of the rank-`r`
layer, and let `A=(A_0,...,A_(W+d-1))` be nonzero with

\[
 D^dA=T,
 \qquad
 T_i=\bigcup_{p=i}^{i+d}A_p.                          \tag{2.1}
\]

### Proposition 2.1 (owner projection and boundary no-go)

Every interval union of `A` having rank greater than `r` is an interval union
of `T`.  More precisely, for every `0<=u<=v<W+d` with
`|union_(p=u)^v A_p|>r`, there are `0<=i<=j<W` such that

\[
 \bigcup_{p=u}^vA_p=\bigcup_{h=i}^jT_h.               \tag{2.2}
\]

Conversely, every owner interval has the literal source witness

\[
 \bigcup_{h=i}^jT_h=\bigcup_{p=i}^{j+d}A_p.           \tag{2.3}
\]

Therefore no choice of the `d` source boundary cells, and no positive value
of the scalar deadline slack, can realize an upper target absent from
`IntOR(T)` while (2.1) is kept fixed.

#### Proof

Equation (2.3) follows by taking the union of the windows in (2.1).
For (2.2), an interval of at most `d` source cells is contained in at least
one of the displayed `(d+1)`-windows, including at the two boundaries, and
therefore has union contained in one rank-`r` owner.  Hence an upper interval has length at
least `d+1`.  The complete `(d+1)`-windows contained in it have starts
`u,...,v-d`; their source ranges cover the original interval, and their
unions are exactly the corresponding consecutive owners.  This proves
(2.2).  This is the local upper-projection lemma from the exact
carrier/compiler factorization.  The last assertion follows immediately.
QED.

The lower deadline slack is

\[
 \sigma=dW+{d+1\choose2}-
       \sum_{s=1}^{r-1}{k\choose s}.                  \tag{2.4}
\]

It counts excess **short lower-interval occurrences**.  Upper targets use
the owner interval tower (and source intervals longer than the lower range).
Thus there is no valid ledger operation which subtracts `|R|` from `sigma`.
Even when `sigma>|R|`, Proposition 2.1 forces the upper order/seam condition
first.

There is a second, architecture-free obstruction to interpreting `sigma` as
literal upper-cell capacity.  Apply the rank-separation deadline theorem at
cutoff `s=r`.  If a word covers the complete ideal through rank `r` and has
`H_(>r)` letters of rank greater than `r`, then

\[
                 |A|\ge H_{>r}+W+d=B(k)+H_{>r}.      \tag{2.5}
\]

Consequently an equality-length word has no high-rank letter at all, and
each literal high-rank repair letter carries an unavoidable unit of length.
This does not say that one high letter can witness only one upper target; it
says exactly that high letters cannot be hidden inside the lower deadline
slack.  The only zero-cost repair in the flat-middle architecture is to make
the casualty an interval of rank-at-most-`r` letters, equivalently by
Proposition 2.1 an owner interval of the final `T`.

For scale only, the exact values

\[
\begin{array}{c|rrrrrr}
k&11&12&13&14&15&16\\ \hline
d&3&2&3&2&3&3\\
\sigma&369&266&1059&392&2928&12284
\end{array}                                           \tag{2.6}
\]

are all positive and much larger than the relevant constant-component ray
lists.  This finite arithmetic does not supply a Hall inequality and is not
used in any proof below.

## 3. The exact multi-seam upper condition

Fix a permutation `pi` of the fragments and concatenate them without
changing their interiors:

\[
 T_\pi=P_{\pi(1)}P_{\pi(2)}\cdots P_{\pi(b)}.         \tag{3.1}
\]

For one fragment define suffix and prefix unions

\[
 L_{a,s}=\bigcup_{u=s}^{n_a-1}X_{a,u},\qquad
 R_{a,t}=\bigcup_{u=0}^{t}X_{a,u}.                   \tag{3.2}
\]

For `i<j`, define its exact multi-seam grid

\[
 \mathcal G_\pi(i,j)=
 \left\{
 L_{\pi(i),s}\cup
 \bigcup_{h=i+1}^{j-1}V_{\pi(h)}\cup
 R_{\pi(j),t}:
 0\le s<n_{\pi(i)},\ 0\le t<n_{\pi(j)}
 \right\}.                                          \tag{3.3}
\]

For adjacent pieces write `G(a,c)` for the same grid with no intermediate
whole fragment.

### Theorem 3.1 (pointwise multi-seam repair criterion)

Assume every upper target outside `R=union_a R_a` retains a witness wholly
inside a fragment.  Then `T_pi` is upper-complete if and only if

\[
 \boxed{
 \mathcal R\subseteq
 \bigcup_{1\le i<j\le b}\mathcal G_\pi(i,j).}
                                                               \tag{3.4}
\]

Here targets already occurring in a fragment may harmlessly be included on
the right as well.

#### Proof

An interval of `T_pi` which is not internal to one fragment begins in a
suffix of its first fragment, contains every whole intervening fragment,
and ends in a prefix of its last fragment.  Its union is exactly (3.3).
Conversely every expression in (3.3) is the union of that literal interval.
All noncasualties retain their internal witnesses, giving (3.4).  QED.

Condition (3.4) is **pointwise**.  All physical intervals of one fixed word
coexist.  They are not unit-capacity seam resources, they may overlap, and
one seam grid may realize many different casualty masks.  Formally, the
target-to-interval host families for two distinct masks are disjoint because
one interval has one union label.  Hence their occurrence-level SDR exists
automatically exactly when every family is nonempty.  What would be a false
strengthening is to give each *seam* capacity one per casualty.

### Corollary 3.2 (when multi-seam intervals reduce to adjacent seams)

Assume every complete fragment has coordinate union `[k]`:

\[
 V_a=[k]\quad(1\le a\le b).                          \tag{3.5}
\]

Every proper target `Y!=[k]` witnessed by a crossing interval crosses
exactly one seam.  Hence (3.4) reduces to

\[
 \mathcal R\setminus\{[k]\}
 \subseteq\bigcup_{i=1}^{b-1}
     \mathcal G(\pi(i),\pi(i+1)).                    \tag{3.6}
\]

The full target `[k]` is already witnessed by the whole owner path.

#### Proof

An interval crossing at least two seams contains one whole intermediate
fragment, whose union is `[k]` by (3.5).  Its union is therefore `[k]`.
QED.

Thus component-fullness is a simple explicit hypothesis under which a
one-seam socket theorem is complete for proper casualties.  Without it,
multi-seam grids in (3.3) must not be discarded.

### Proposition 3.3 (physical q-slot count)

Let `Sigma` be the `b-1` inserted seams of a concatenation, and let
`J_(Sigma,q)` be the owner intervals having exactly `q` transitions and
crossing at least one inserted seam.  Then

\[
                   |\mathcal J_{\Sigma,q}|\le q(b-1).              \tag{3.7}
\]

If every retained fragment has at least `q` vertices, equality holds.  At
depth `q`, the protected-ray injection gives at most `b` old-lost labels.
After `(E1)` removes `q=2`, one has `q>=3`, and therefore for `b>=2`

\[
                         q(b-1)\ge b.                \tag{3.8}
\]

Thus the scalar number of minimal-width seam-crossing slots is already
large enough.  The remaining upper obstruction is label coherence, not a
shortage of interval positions.

#### Proof

A fixed seam edge belongs to at most `q` intervals of `q` consecutive
edges, according to the position of that seam among the `q` edges.  Summing
over the `b-1` seams proves (3.7).  If every fragment has at least `q`
vertices, each seam is at least `q` vertices from the two global ends and
two consecutive seams are separated by at least `q` edges.  It therefore
belongs to exactly `q` such intervals, and no one interval contains two
seams; equality follows.  The loss and arithmetic statements are Theorem
4.4 of the protected-ray report and `q(b-1)>=b`.  QED.

For `b=1` there is no inserted seam slot.  A locked ray must then have a
second retained occurrence, be repaired by changing the owner chronology,
or be paid for literally.

## 4. Protected outgoing sockets and the acyclic SDR theorem

We now impose a narrower but useful architecture.  The casualty chain of
fragment `a` must be repaired at the seam immediately after `a`.  A directed
pair `a->c` is called an **upper socket** if

\[
 \mathcal R_a\subseteq\mathcal G(a,c).               \tag{4.1}
\]

Here and throughout this section the chain is first normalized to

\[
                 \mathcal R_a^\circ=\mathcal R_a\setminus\{[k]\}; \tag{4.1a}
\]

we suppress the circle in the notation.  The full mask `[k]` is witnessed
by the whole final owner path and never needs an outgoing socket.  Without
this normalization, the theorem below is still exact for the deliberately
stronger requirement that every assigned label be repaired immediately
after its assigned fragment, but its terminal condition would not be
minimal for actual upper completeness.

It is called **seam-locally legal** if, in addition, the requested seam class
is obeyed (Johnson adjacency when required) and the pairwise residence test
below holds.  This is always sufficient for final residence and is exact
under the stated no-through-coordinate hypothesis.

The local sufficient condition has the following coordinate test.  Let `ell_a^-(z)` be the
terminal positive-run length of coordinate `z` in `P_a`, zero when
`z notin x_a`, and let `ell_c^+(z)` be the initial positive-run length in
`P_c`.  At an internal seam `a|c`, consider

\[
 \ell_a^-(z)+\ell_c^+(z)\ge d+1
 \quad\hbox{for every }z\in x_a\cap X_{c,0},          \tag{4.2a}
\]

\[
 \ell_a^-(z)\ge d+1
 \quad(z\in x_a\setminus X_{c,0}),
 \qquad
 \ell_c^+(z)\ge d+1
 \quad(z\in X_{c,0}\setminus x_a).                  \tag{4.2b}
\]

If all nonboundary runs inside the fragments are already legal, these tests
are sufficient.  They are also necessary when no coordinate runs through a
whole fragment,

\[
 \bigcap_{j=0}^{n_a-1}X_{a,j}=\varnothing
 \quad(1\le a\le b).                                \tag{4.2c}
\]

Under (4.2c), every run crossing `a|c` ends in one of its two incident
fragments, so its length is exactly a quantity in (4.2a)--(4.2b).  Without
(4.2c), a coordinate may pass through several whole fragments; (4.2) remains
a safe local sufficient test but can reject a globally long run.  Exact
legality must then be checked on the full concatenated order.  Runs at the
two global endpoints remain boundary runs.  The separate maximal-erosion
nonemptiness condition is still required for `D^dP=T`.

Let `N(a)` be the set of `c` for which `a->c` is a seam-locally legal upper
socket.  If
`R_a` is empty, (4.1) is vacuous and `N(a)` is simply the legal seam list.

### Theorem 4.1 (exact acyclic successor-SDR criterion)

There is a concatenation of all `b` fragments into one seam-locally legal linear path
which repairs every chain `R_a` at the seam immediately after `a` if and
only if there is a terminal fragment `t` such that

\[
 \mathcal R_t=\varnothing                              \tag{4.3}
\]

and an injective map

\[
 f:[b]\setminus\{t\}\longrightarrow[b],
 \qquad f(a)\in N(a),                                \tag{4.4}
\]

whose directed arcs `a->f(a)` contain no directed cycle.

Equivalently, there are `t` and a total order `prec` with `t` maximal such
that the **forward lists**

\[
 N^+_\prec(a)=\{c\in N(a):a\prec c\}                 \tag{4.5}
\]

satisfy the ordinary Hall inequalities

\[
 \boxed{
 \left|\bigcup_{a\in S}N^+_\prec(a)\right|\ge|S|
 \quad\hbox{for every }S\subseteq[b]\setminus\{t\}.}
                                                               \tag{4.6}
\]

#### Proof

Any desired concatenation has one terminal `t`, which has no outgoing seam;
hence its assigned chain must be empty in this architecture.  Mapping every
other fragment to its successor gives (4.4).  Successors are distinct, and
the arcs form one directed Hamilton path, hence are acyclic.

Conversely, the graph of an injective map (4.4) has outdegree one away from
`t`, outdegree zero at `t`, and indegree at most one.  It has `b-1` arcs.
If it is acyclic, its components are directed paths.  Since only `t` has
outdegree zero, there is only one component; it is a Hamilton path ending at
`t`.  Each of its seams is legal and (4.1) repairs the preceding chain.

Given an acyclic map, take a topological order of its arcs; `t` is maximal,
and the selected representatives prove (4.6).  Conversely, Hall's theorem
applied to the forward lists gives an injective map.  Every selected arc is
strictly forward, so it is acyclic.  This proves the equivalence.  QED.

This is the minimal exact strengthened `(E1)` condition inside the declared
one-outgoing-seam architecture.  It uses `b-1` unit-capacity **successor
fragment sockets**, not one unit port per casualty.  A selected seam may
simultaneously realize the whole nested chain of at most `k-r-2` casualties.
The unit capacity in (4.4) expresses that one fragment start has only one
predecessor; it is not a capacity restriction on its many interval witnesses.

Call (4.3)--(4.6), together with the literal grid and seam tests, `(E1-ray)`.

## 5. The common lower compiler is an independent Hall gate

Let an `(E1-ray)` solution give a final owner path `T`.  Assume its maximal
depth-`d` erosion is nonempty and satisfies `D^dP=T`.

### Theorem 5.1 (upper/lower product interface)

1. `(E1-ray)` and the retained interiors make every upper target an owner
   interval of `T`.
2. If `COMP_d(T)` is feasible, any one common nonzero antecedent `A` solving
   it is already upper-complete by (2.3).  No further upper/lower assignment
   is needed.
3. In the robust-core branch, let `C` be a protected common-`Q` core and let
   each residual lower target `S` have its exact safe one-cell list `N_C(S)`.
   Put

   \[
   \delta=\max_{\mathcal X}
       \left(|\mathcal X|-\left|\bigcup_{S\in\mathcal X}N_C(S)\right|\right)_+.
                                                               \tag{5.1}
   \]

   Then a matching installs all but exactly `delta` residual lower targets,
   and literal appendage of the unmatched masks gives

   \[
              \nu(k)\le B(k)+\delta.                 \tag{5.2}
   \]

More generally, for any legal ordering let `tau` be the number of distinct
explicit upper casualties not contained in its exact multi-seam grids, and
define the exact common-compiler deletion number by

\[
 \lambda_d(T)=
 \min_{\substack{A_p\ne\varnothing\\D^dA=T}}
 \#\left\{S:1\le|S|<r,\ S\notin\operatorname{IntOR}(A)\right\},    \tag{5.3a}
\]

with value infinity if the fibre is empty.  Then

\[
 \boxed{\nu(k)\le B(k)+\tau+\lambda_d(T).}            \tag{5.3}
\]

#### Proof

The upper claims are Theorems 3.1 and 4.1 followed by (2.3).  The robust
lower statement is the deficiency form of Hall's theorem and the safe
one-cell augmentation theorem.  In general choose an antecedent attaining
`lambda_d(T)` and append the missing lower masks and the `tau` missing upper
masks.  Old witnesses remain in the prefix.  QED.

All lists and maximal erosion data in (5.1) must be recomputed after the
final rethreading.  Old componentwise lists or the scalar slack (2.4) do not
imply (5.1).  This is the exact separation requested here:

* upper repair is the pointwise owner-grid condition (3.4), with `(E1-ray)`
  an exact acyclic-SDR specialization;
* lower realization is `COMP_d(T)`, or the common-`Q` Hall condition (5.1)
  in the robust branch;
* residence is the seam test (4.2) plus nonempty maximal erosion;
* scalar deadline slack is neither an upper port nor a substitute for lower
  Hall.

### Corollary 5.2 (deterministic interval-list Hall test)

In the robust-core branch, suppose the safe lower port set is linearly
ordered and every residual list is an interval `[l_S,u_S]`.  Then `delta=0`
if and only if

\[
 \#\{S:[l_S,u_S]\subseteq[s,t]\}\le t-s+1
 \quad(1\le s\le t\le |P|).                         \tag{5.4}
\]

The matching is obtained by processing targets in nondecreasing right
endpoint and assigning the earliest unused allowed port.  For the exact two
boundary prefix lists

\[
 N_C(S)=\{L_1,\ldots,L_{\ell_L(S)}\}
       \cup\{R_1,\ldots,R_{\ell_R(S)}\},             \tag{5.5}
\]

where all `L_i,R_j` are pairwise distinct physical ports,

the condition is equivalently the finite family

\[
 \#\{S:\ell_L(S)\le a,\ \ell_R(S)\le c\}\le a+c
 \quad(0\le a,c\le d).                              \tag{5.6}
\]

#### Proof

Necessity of (5.4) is Hall applied to targets whose whole lists lie in one
port interval.  If Hall fails, decompose the union of the offending interval
lists into disjoint interval components.  Each connected list lies in one
component, and one component contains more lists than ports, contradicting
(5.4).  The usual exchange proof gives the stated earliest-deadline greedy
matching.  Formula (5.6) is the two-prefix Hall-deficiency theorem: every
neighbourhood union is determined by the largest used left and right
prefixes.  QED.

This corollary applies only after one common-`Q` robust core has made every
listed singleton augmentation transparent.  For unrestricted `COMP_d(T)`,
ordinary Hall can miss a positive-coordinate or nonempty-letter conflict.

## 6. Quantified consequences and scope

Assume `(E1)` protects depth two and `b=O(1)`.

* Blind literal repair costs at most `b max(k-r-2,0)=O(k)` cells.
* `(E1-ray)` replaces those up to `O(k)` casualty cells by only `b-1`
  selected seam sockets and costs zero extra cells at the upper layer.
* If the final robust lower Hall defect is `delta`, the total proved overhead
  is exactly bounded by `delta`; with full common compiler it is zero.
* If `(E1-ray)` fails, (5.3) still gives `B(k)+O(k)` once `b=O(1)` and the
  lower defect is `O(k)`.

No claim is made that PBBS automatically satisfies `(E1-ray)`.  Fixed-width
all-depth support classifies the casualty masks but does not supply compatible
successor flags.  Residence does not imply the grid inclusions.  Positive
deadline slack, even when numerically larger than the ray list, does not
alter `IntOR(T)`.  Without component-fullness, multi-seam witnesses must be
tested by (3.3), and the one-outgoing-seam SDR is only a sufficient protected
subarchitecture.  These are the exact remaining interfaces rather than an
unproved absorption assertion.

## 7. Independent audit

An independent derivation, written without using the component-order proof
of Sections 3--4, is

```text
MATH_THEOREM_R_OUTWARD_RAY_PORT_SDR_AND_LOWER_COMPILER_SEPARATION_20260730.md
  4517a906ae3bd9673038f2ede6b091b405d671d0133b85d8bf0faf0cc20c034e
```

It separately proves the source/owner occurrence bijection, the disjoint
host-family reduction, the interval-list Hall theorem, and the additive
upper/lower defect bound.  A second adversarial pass checked the following
scope points.

1. The source boundary positions are not upper ports while `T` is fixed.
2. Occurrence-level host sets are disjoint; seam-level capacity one is not
   valid because one seam supplies a whole grid.
3. Multi-seam intervals are retained in (3.3).  Terminal emptiness is
   required only in the one-outgoing-seam specialization.
4. The numerical values in (2.6) are calibrations only; no assertion that
   `sigma>0` for every future dimension is used.
5. Ordinary lower Hall is invoked only after the robust common-`Q`
   transparency hypothesis.  Unrestricted `COMP_d(T)` remains the exact
   condition outside that branch.
6. The outgoing-SDR chains omit `[k]`, which is always witnessed by the
   whole owner path, and the two-prefix formula uses distinct physical
   left/right ports.  Without distinctness its right side must be replaced
   by `|{L_1,...,L_a} union {R_1,...,R_c}|`.

No finite search, SAT solver, remote computation, or web input was used.
