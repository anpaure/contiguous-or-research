# Swapped SCD forests have exact colored component switches, but they only transfer connector slack between the two special coordinates

Date: 2026-08-01  
Lane: swapped SCD phase forests / colored symmetric difference / endpoint
connector cut  
Status: unconditional switch formalism and per-component sum invariant;
authenticated census through `m=9`.  The saved swapped-forest fibres cannot
repair both special-coordinate connector cuts, even before acyclicity.

## 0. Outcome

Let `F^-=F(a,z)` be an upper-exact, lower-injective directed SCD linear
forest on all rank-`m` owners, with its rooted `M_0` relation pairing every
terminal owner with its unused lower colour, and let

\[
                           F^+=\tau F^-,\qquad \tau=(a\ z).     \tag{0.1}
\]

Close every directed path of each forest by one typed dummy arc from its
terminal owner to its source owner.  Label corresponding red and swapped
blue dummy arcs by the same dummy upper colour.  A dummy arc also carries
the component's missing lower colour.  The resulting `\widehat F^-` and
`\widehat F^+` are perfect matchings on four resource shores:

* all rank-`(m-1)` lower colours;
* all typed tail owners;
* all typed head owners; and
* the true upper layer plus `C=Cat_m` dummy upper colours.

Therefore their two-copy colored incidence overlay decomposes into
connected components which may be switched independently while preserving
all four complete resource shores.  This is not set-theoretic symmetric
difference: coincident red and blue physical atoms remain distinct colored
copies.

For one colored component `Gamma`, let its red-to-blue change in the
connector slack

\[
                         \kappa_t=S_t-H_t+1                         \tag{0.2}
\]

be `Delta kappa_t(Gamma)`.  Then

\[
              \boxed{\Delta\kappa_a(\Gamma)+
                     \Delta\kappa_z(\Gamma)=0.}                  \tag{0.3}
\]

Thus colored component switches can transfer slack from `a` to `z`, or
back, but cannot create total two-coordinate slack.

The authenticated SCD witnesses at `m=4,...,9` all have

\[
                         \kappa_a(F^-)+\kappa_z(F^-)<0.           \tag{0.4}
\]

Consequently no subset of their colored components can satisfy both
connector cuts `kappa_a>=0` and `kappa_z>=0`, even if graphic acyclicity is
ignored.  Almost every individual nonzero transfer component is nevertheless
forest-safe: all are safe through `m=8`, and `488/489` are safe at `m=9`.

This is the precise boundary between the positive two-stratum endpoint-hole
theorem and the old directed connector obstruction.  The former repairs the
undirected coordinate cocycle `E=H+2c`; neutral swapped-forest switches do
not increase `kappa_a+kappa_z`.  The audited paired three-for-three rethread
has only one `z`-cut unit after its displaced ordinary target bundle is
restored, and no current fixed-`M_0` catalogue supplies a proved gain-two
packet.  What is still required is a packet with positive **total**
two-coordinate current, or a base outside the standard one-stratum SCD
phase grammar.

## 1. Perfect augmented factors

Let a directed component of `F^-` be

\[
                         T_0\to T_1\to\cdots\to T_q.             \tag{1.1}
\]

Its missing lower colour is the terminal rooted tail `K`, and its physical
source owner is `T_0`.  Add a dummy atom

\[
                         d=(K,\delta_i,T_q,T_0),                  \tag{1.2}
\]

where `delta_i` is a private dummy-upper label.  Real Johnson atoms have
the usual four resources

\[
                         (T\cap H,T\cup H,T_{tail},H_{head}).    \tag{1.3}
\]

### Lemma 1.1 (four complete shores)

The augmented set `widehat F^-` uses every lower colour, typed tail owner,
typed head owner and expanded upper colour exactly once.  The same holds
for `widehat F^+`.

#### Proof

The real forest uses every true upper once and `U=W-C` distinct lower
colours.  Its `C` missing lower colours are exactly the component-terminal
tails.  Each real path uses every owner once as a typed tail except its
terminal and once as a typed head except its source.  The dummy atom (1.2)
fills precisely these three missing resources and one private dummy upper.
Summing over the `C` components completes all four shores.  Coordinate
swap preserves the statement. \(\square\)

Match dummy labels equivariantly: the dummy closing a red component and the
dummy closing its swapped blue component both use the same `delta_i`.

## 2. Exact colored-component cube

Make a bipartite incidence graph whose atom vertices are the red atoms of
`widehat F^-` and the blue atoms of `widehat F^+`.  For each of the four
resource shores, join the unique red and blue atoms using that resource.
Resource vertices have been suppressed; parallel incidence edges are
allowed, and coincident physical atoms remain separate colored vertices.

### Theorem 2.1 (independent component switches)

Let `Gamma_1,...,Gamma_s` be the connected components of this colored
incidence graph.  For every `x in {0,1}^s`, taking all red atoms of
`Gamma_i` when `x_i=0` and all blue atoms when `x_i=1` gives another perfect
four-resource augmented factor.  Every perfect four-shore augmented factor
supported on the red/blue union has this form.

#### Proof

No resource edge crosses a connected component.  Inside one component,
every resource occurs once in red and once in blue.  Replacing the complete
red shore by the complete blue shore therefore preserves every resource
exactly.  Different components are resource-disjoint, so all switches
compose.  Conversely, on each resource edge the two endpoint-selection
bits sum to one.  Propagating this equality through a connected component
forces every atom in that component to use the same phase. \(\square\)

After the switches, delete the selected dummy atoms.  The remaining real
support is automatically upper-exact, lower-injective and of maximum
indegree/outdegree one.  Its hole family and endpoint owners are precisely
the lower, tail and head resources carried by the selected dummies.

## 3. Exact component signature

For a dummy atom `d`, write

\[
 w_t(d)={\bf1}_{t\in\operatorname {head}(d)}
        -{\bf1}_{t\in\operatorname {lower}(d)}.                 \tag{3.1}
\]

The head of a dummy is the physical source endpoint, while its lower
resource is the hole.  Hence, for a red-to-blue switch,

\[
 \boxed{
 \Delta\kappa_t(\Gamma)
  =\sum_{d\in\Gamma\cap D^+}w_t(d)
   -\sum_{d\in\Gamma\cap D^-}w_t(d).}                         \tag{3.2}
\]

This is the exact computable component weight requested by the connector
cut.  More separately,

\[
\begin{aligned}
 \Delta H_t(\Gamma)
   &=|\{d\in D^+\cap\Gamma:t\in\operatorname {lower}(d)\}|
     -|\{d\in D^-\cap\Gamma:t\in\operatorname {lower}(d)\}|,\\
 \Delta S_t(\Gamma)
   &=|\{d\in D^+\cap\Gamma:t\in\operatorname {head}(d)\}|
     -|\{d\in D^-\cap\Gamma:t\in\operatorname {head}(d)\}|.
\end{aligned}                                                   \tag{3.3}
\]

### Theorem 3.1 (per-component transfer law)

Every colored component satisfies (0.3).

#### Proof

A component containing no dummy atom has zero signature.  If `Gamma`
contains a red dummy, the shared dummy-upper label joins it directly to the
corresponding swapped blue dummy.  The involution which swaps red and blue
and simultaneously applies `tau=(a z)` therefore maps `Gamma` to itself.

For every paired dummy, the blue `a`-weight is the red `z`-weight and the
blue `z`-weight is the red `a`-weight.  Substitution in (3.2) gives

\[
                         \Delta\kappa_a(\Gamma)
                        =-\Delta\kappa_z(\Gamma).
\]

This proves (0.3).  The same involution gives
`Delta kappa_q(Gamma)=0` for every ordinary coordinate
`q notin {a,z}`. \(\square\)

### Corollary 3.2 (exact subset system)

For a base forest `F^-` and component bits `x_i`,

\[
 \kappa_t(x)=\kappa_t(F^-)+
              \sum_i x_i\Delta\kappa_t(\Gamma_i),              \tag{3.4}
\]

and `kappa_a(x)+kappa_z(x)` is independent of `x`.  A necessary and
sufficient scalar condition for some switch vector to make both special
cuts nonnegative is

\[
 \kappa_a(F^-)+\kappa_z(F^-)\ge0
\]

together with the one-dimensional subset-sum condition

\[
 -\kappa_z(F^-)
 \le \sum_i x_i\Delta\kappa_z(\Gamma_i)
 \le \kappa_a(F^-).                                      \tag{3.5}
\]

Graphic acyclicity is an additional constraint.

## 4. Exact acyclicity row

Every augmented hybrid is a directed permutation on the physical owners.
Deleting the dummy arcs gives a linear forest exactly when every directed
cycle of the augmented permutation contains at least one dummy.

Equivalently, consider a phase-labelled, component-consistent all-real
directed cycle `Q`: all phase-sensitive atoms of `Q` lying in one
`Gamma_i` must come from a single phase `b_i(Q)`.  A candidate demanding
both red and blue atoms from one component is unrealizable and is omitted;
coincident physical arcs are retained as colored copies.  Let `I(Q)` be
the phase-sensitive components used by `Q`.  Then impose
the lazy clause

\[
                         \bigvee_{i\in I(Q)}
                         [x_i\ne b_i(Q)].                       \tag{4.1}
\]

These cycle-hit clauses are necessary and sufficient.  They are the exact
SAT interface for searching the colored cube; no generic subtour surrogate
is needed.

## 5. Authenticated finite census

The O3 C++ checker reconstructed the saved SCD forests independently from
their selected-option tables, verified both complete resource factors,
built the four-shore colored incidence components, replayed (3.2), and
tested every nonzero component as a single switch by a fresh disjoint-set
forest check.  All runs were on the H100 CPU host.

| `m` | colored components | nonzero `Delta kappa` | max atoms / dummies | base `(kappa_a,kappa_z)` | invariant sum | forest-safe nonzero singles |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 9 | 4 | 11 / 4 | `(2,-3)` | -1 | 4 / 4 |
| 5 | 29 | 8 | 19 / 4 | `(1,-13)` | -12 | 8 / 8 |
| 6 | 147 | 28 | 59 / 14 | `(6,-47)` | -41 | 28 / 28 |
| 7 | 591 | 80 | 81 / 19 | `(1,-164)` | -163 | 80 / 80 |
| 8 | 2222 | 185 | 720 / 144 | `(-68,-571)` | -639 | 185 / 185 |
| 9 | 8762 | 489 | 3959 / 770 | `(-467,-2001)` | -2468 | 488 / 489 |

Every nonzero signature was of the form

\[
                         (-q,+q),\qquad q>0.                     \tag{5.1}
\]

The total transferable masses `sum q` were respectively

\[
                         5,14,53,165,503,1534.                  \tag{5.2}
\]

The `q=1` component counts were

\[
                         3,2,17,47,102,260.                     \tag{5.3}
\]

Thus the cube has abundant fine-grained slack transport and almost no
single-switch graphic obstruction.  Nevertheless every invariant sum in
the table is negative, proving the two-cut no-go for these fixtures without
enumerating subsets or adding (4.1).

## 6. Exact scope and next move

The no-go is for neutral component switching between each saved forest and
its coordinate swap.  It is not a no-go for:

1. choosing a base outside the standard one-stratum SCD phase grammar with
   `kappa_a+kappa_z>=0` (inside that grammar the exact bound
   `kappa_a+kappa_z<=c-I+2<0` holds for every `m>=6`);
2. a palette-preserving service packet with positive total gain;
3. switching between non-swapped factors; or
4. a support-first decorated factor outside the SCD phase fibre.

The immediate proof target is therefore not more neutral switching.  It is
to construct a base forest with nonnegative two-coordinate sum, or compose
the colored cube with a new, literally audited positive-total-current
packet.  The paired ear alone does not have that advertised gain.  Once the
sum obstruction is lifted, (3.5) and the lazy clauses (4.1) are the complete
residual finite problem.
