# Same-phase alternating \(C_6\)'s: monodromy, carriers, and an exact host bank

Date: 2026-07-26

Method: pure mathematics only.  No finite search, solver, program, or web
input is used.

## 0. Outcome

Every simple six-cycle in the middle-levels inclusion graph is a
three-petal common-core star.  Toggling one selected half at one path phase
preserves the complete \(X/Y\) resource ledger and cyclically permutes
three equal-length tails in the abstract open-path ledger.  Its formal
endpoint monodromy has order three.  Three commonly labelled copies have
identity formal monodromy if and only if their orientations agree.

This is not by itself a physical fixed-exterior wreath substitution.
Geodesicity forces a nonidentity twist to be trivial in every ordinary
fixed-exterior minimum slab.  A literal use of the hexagon must instead be
one jointly zero-monodromy phase packet, or an exterior-moving packet with
its complete crossing-collar ledger.

At the first up-edge the aggregate first-insertion and first-deletion
histograms are both invariant.  The row-resolved joint
deletion/insertion carrier can nevertheless be nonzero.

There are two opposite occurrence theorems.

1.  The canonical MSW/Chung--Feller factor contains no same-phase
    alternating \(C_6\), at any phase and in either incidence matching.
    In fact it contains no same-phase directed common-core cycle of any
    length.
2.  For every \(s\ge3\) there is an explicit noncanonical exact
    \(\mathcal D_s\)-port factor containing \(C_{s-3}\) pairwise
    vertex-disjoint same-phase clean \(C_6\) certificates.  They touch
    \(3C_{s-3}\) roots, and
    \[
       \frac{C_{s-3}}{C_s}\longrightarrow\frac1{64},
       \qquad
       \frac{3C_{s-3}}{C_s}\longrightarrow\frac3{64}. \tag{0.1}
    \]

Thus positive-density occurrence is possible, but not in the canonical
factor.  Toggling the disjoint bank gives only an abstract open-path
ledger with disjoint three-cycle monodromies, not an odd-graph factor and
not a fixed-exterior slab.  A jointly geodesic zero-monodromy construction
with all crossing collars is still required before this bank becomes an
exact factor trade.

## 1. Set-theoretic classification

Let \(M(J)\) be the inclusion graph on
\(\binom Js\sqcup\binom J{s+1}\), where \(|J|=2s\).

### Theorem 1.1 (all simple six-cycles)

Every simple \(C_6\subset M(J)\), uniquely up to relabelling and cyclic
reversal, is

\[
 Ka-Kab-Kb-Kbc-Kc-Kca-Ka,                            \tag{1.1}
\]

where \(|K|=s-1\) and \(a,b,c\notin K\) are distinct.  Conversely (1.1)
is always a simple \(C_6\).

#### Proof

The three lower vertices are pairwise adjacent in the Johnson graph.
A Johnson triangle either has one common \((s-1)\)-core or consists of
three \(s\)-subsets of one common \((s+1)\)-set.  In the second case all
three pairwise unions are the same upper vertex, contradicting simplicity.
The first case is exactly (1.1).  \(\square\)

Suppose the old selected up-edges are

\[
 Ka-Kab,qquad Kb-Kbc,qquad Kc-Kca,                  \tag{1.2}
\]

and replace them by the other half

\[
 Kb-Kab,qquad Kc-Kbc,qquad Ka-Kca.                  \tag{1.3}
\]

The primitive signed edge circuit is

\[
 z=e_{Kb,Kab}+e_{Kc,Kbc}+e_{Ka,Kca}
   -e_{Ka,Kab}-e_{Kb,Kbc}-e_{Kc,Kca}.                \tag{1.4}
\]

Every lower and upper vertex has signed degree zero.  Hence the two
incidence-resource ledgers are preserved literally, not fractionally.
This is a degree/ownership statement, not complementary endpoint closure.

## 2. Tail monodromy

Cut the three old paths immediately before (1.2).  After (1.3), the prefix
ending at \(Ka\) follows the old tail beginning at \(Kca\); the prefix at
\(Kb\) follows the old tail beginning at \(Kab\); and the prefix at
\(Kc\) follows the old tail beginning at \(Kbc\).  Thus, on the labels
\(a,b,c\), the twist is

\[
                           \tau=(a\ c\ b).             \tag{2.1}
\]

The opposite orientation gives \(\tau^{-1}\).  Since all three cuts have
the same phase, the new open components have the old length.  One toggle
is an equal-length twisted open-path partition, but it is neither an
untwisted port factor nor a physical fixed-exterior minimum-wreath slab.

### Theorem 2.1 (fixed-exterior obstruction)

Let a nominal local rank-\(r\) slab have fixed exterior \(O\), start at
\(O\cup P\), and end at \(O\cup(J\setminus\tau(P))\).  Its endpoint
Johnson distance is

\[
 d_J\bigl(O\cup P,O\cup(J\setminus\tau(P))\bigr)
                         =|P\cap\tau(P)|.              \tag{2.2}
\]

An \(r\)-step segment of a minimum wreath is geodesic.  Hence such a slab
exists only when \(|P\cap\tau(P)|=r\), equivalently \(\tau(P)=P\).

More generally, if the exterior changes from \(O_L\) to \(O_R\) and
\(e=|O_L\setminus O_R|\), the necessary geodesicity equation is

\[
                         e=|P\setminus\tau(P)|.        \tag{2.3}
\]

#### Proof

The elements removed between the two boundary states are the exterior
losses \(O_L\setminus O_R\) and the local elements
\(P\cap\tau(P)\).  Their total is
\(e+|P\cap\tau(P)|\).  Setting this distance equal to the slab length
\(r\) gives (2.3), and fixed exterior gives the stated rigidity.
\(\square\)

### Theorem 2.2 (formal three-copy monodromy)

For three serial copies transported to one common strand labelling, let
their orientations be \(\tau^{\varepsilon_j}\),
\(\varepsilon_j\in\{1,-1\}\).  The formal endpoint monodromy is the
identity if and only if all three orientations agree.

#### Proof

The product is \(\tau^{\varepsilon_1+\varepsilon_2+\varepsilon_3}\).
Since \(\tau\) has order three, this is the identity exactly when the sum
is \(3\) or \(-3\), not when it is \(1\) or \(-1\).  \(\square\)

For nontrivial identifications between packets, each local twist must first
be conjugated into a common label set.  Merely having three abstract
hexagons is not enough.  Theorem 2.1 forbids interpreting them as three
independent fixed-exterior slabs.  A positive construction must be one
joint geodesic packet, or move the exterior according to (2.3) and pay
every crossing collar.

## 3. Exact first-edge carrier

Put \(u_0=a,u_1=b,u_2=c\), with indices modulo three, and

\[
 X_i=K+u_i,qquad Y_i=K+u_i+u_{i+1}.                  \tag{3.1}
\]

Suppose the retained down-edge after \(Y_i\) deletes \(d_i\), so its next
lower state is \(Y_i-d_i\).  For the toggled paths to be simple Johnson
geodesics one must have

\[
                              d_i\in K.                \tag{3.2}
\]

Indeed, deleting \(u_i\) would make the retained next state equal the
new lower endpoint of the other half of the hexagon; deleting the newly
inserted \(u_{i+1}\) is not an old forward exchange.  Thus only a core
coordinate can be deleted.

The old and new first-edge pairs \((\text{deletion},\text{insertion})\)
are

\[
\begin{array}{c|c|c}
\text{root}&\text{old}&\text{new}\\ \hline
Ka&(d_a,b)&(d_c,c)\\
Kb&(d_b,c)&(d_a,a)\\
Kc&(d_c,a)&(d_b,b).
\end{array}                                             \tag{3.3}
\]

Consequently the row-resolved insertion carrier is

\[
 e_c-e_b,qquad e_a-e_c,qquad e_b-e_a,                \tag{3.4}
\]

and the deletion labels are cyclically permuted.  Therefore

\[
                    \boxed{\Delta I=0,\qquad\Delta D=0.}       \tag{3.5}
\]

The joint carrier need not vanish:

\[
\begin{aligned}
 \Delta_{\rm joint}={}&
 e_{(d_c,c)}+e_{(d_a,a)}+e_{(d_b,b)}\\
 &-e_{(d_a,b)}-e_{(d_b,c)}-e_{(d_c,a)}.               \tag{3.6}
\end{aligned}
\]

With three row-dependent exterior carriers \(O_i\), the lower singleton
action is

\[
 \sum_{i\in\mathbb Z_3}
 \left(e_{O_i\cup\{u_{i-1}\}}-e_{O_i\cup\{u_{i+1}\}}\right). \tag{3.7}
\]

It vanishes for one common exterior.  Thus a useful packet must expose a
row-resolved or crossing-context carrier; it cannot improve the aggregate
singleton quota of one common-carrier fibre.

The down-half hexagon is dual: first insertions stay fixed rowwise, first
deletions are cyclically reassigned, and their aggregate marginal again
vanishes.

## 4. Canonical MSW obstruction

The canonical up matching is \(X\subset g(X)\).  Reversing the canonical
down matching gives \(X\subset g'(X)\), because \(h^{-1}=g'\).  Both
\(g\) and \(g'\) change a down-step touching height zero into an up-step;
the changed down-step starts at height zero or one.

### Theorem 4.1 (no canonical same-phase common-core cycle)

For every \(s\) and every phase, neither canonical incidence matching
contains a directed common-core cycle.  In particular it contains no
same-phase alternating \(C_6\) or \(C_8\).

#### Proof

Suppose, for \(\gamma\in\{g,g'\}\), that

\[
 \gamma(K+u)=K+u+\sigma(u)                            \tag{4.1}
\]

on a directed cycle of active coordinates, and that all balanced paths
\(K+u\) have the same flaw number.  Let \(p\) be the least active
coordinate, let \(r=\sigma(p)\), and let \(q\) be the predecessor of
\(p\).  Then \(q,r>p\).

Let \(w\) be the deficient path with up-step set \(K\), and let
\(H_w(j)\) be its height immediately before position \(j\).  Since
\(\gamma(K+q)\) selects position \(p\), while \(q>p\),

\[
                          H_w(p)\in\{0,1\}.            \tag{4.2}
\]

Since \(\gamma(K+p)\) selects \(r>p\), the earlier up-step at \(p\)
raises the height there by two, and hence

\[
                   H_w(r)+2\in\{0,1\},
                   \qquad H_w(r)\in\{-2,-1\}.         \tag{4.3}
\]

Compare the balanced paths \(K+p\) and \(K+r\), counting flaws as
up-steps starting below height zero.  The special up-step at \(p\) in
\(K+p\) is nonflawed by (4.2), whereas the special up-step at \(r\) in
\(K+r\) is flawed by (4.3).  Between \(p\) and \(r\), the former path is
two height units above the latter, so every common up-step flawed in the
former is also flawed in the latter.  Outside this interval their heights
agree.  Therefore

\[
                \operatorname{fl}(K+p)
                <\operatorname{fl}(K+r),              \tag{4.4}
\]

contradicting the common phase.  \(\square\)

The obstruction is phase-sensitive.  It does not exclude cross-phase
functional cycles, or same-phase cycles after changing the factor.

## 5. A complete rank-three factor with a root hexagon

Let \(J=[6]\) and use the Dyck roots

\[
                     123,124,125,134,135.              \tag{5.1}
\]

Consider the following five rooted Johnson paths:

\[
\begin{array}{c|cccc}
123&123&234&245&456\\
124&124&145&345&356\\
125&125&235&236&346\\
134&134&136&126&256\\
135&135&156&146&246.
\end{array}                                             \tag{5.2}
\]

Their adjacent-union colours are

\[
\begin{array}{c|ccc}
123&1234&2345&2456\\
124&1245&1345&3456\\
125&1235&2356&2346\\
134&1346&1236&1256\\
135&1356&1456&1246.
\end{array}                                             \tag{5.3}
\]

### Theorem 5.1

Tables (5.2)--(5.3) form an exact \(\mathcal D_3\)-port path factor.
Its three root up-edges

\[
 123-1234,qquad124-1245,qquad125-1235               \tag{5.4}
\]

are one clean same-phase alternating \(C_6\), with common core \(12\)
and active labels \(3,4,5\).

#### Proof

Every adjacent pair in (5.2) differs by one exchange, and each last state
is the complement of its root.  The twenty entries in (5.2) are exactly
all three-subsets of \([6]\): five Dyck roots, their five complements,
and the ten remaining internal states.  The fifteen entries in (5.3) are
exactly all four-subsets of \([6]\).  Hence both resource ledgers are
exact.  Display (5.4), together with the unused incidences to the other
endpoints of \(1234,1245,1235\), is precisely (1.1).  The three edges lie
on three distinct rooted paths and at the same phase.  \(\square\)

Toggling (5.4) changes the three endpoints by the cycle

\[
                         (123\ 125\ 124),              \tag{5.5}
\]

while preserving every \(X\)- and \(Y\)-vertex.

## 6. An all-rank positive-density occurrence bank

For \(s\ge3\), let \(R\) range over \(\mathcal D_{s-3}\) on coordinates
\(7,\ldots,2s\).  The MSW concatenation identity is

\[
             \rho(PR)=\rho(P)\mathbin\Vert(6+\rho(R)). \tag{6.1}
\]

Thus, for each fixed \(R\), the five canonical rows rooted at \(PR\),
\(P\in\mathcal D_3\), first traverse a complete rank-three local factor
and then traverse the common suffix factor.

Replace that canonical rank-three prefix factor by (5.2), independently
for every \(R\), and leave every later transition and every other root
row unchanged.

### Theorem 6.1 (exact host factor and abstract switch bank)

The result is an exact \(\mathcal D_s\)-port factor.  It contains the
pairwise vertex-disjoint same-phase clean hexagons

\[
\begin{aligned}
 123R-1234R-124R-1245R-125R-1235R-123R,
 \qquad R\in\mathcal D_{s-3}.                         \tag{6.2}
\end{aligned}
\]

Hence it contains the certified alternating-cycle occurrence bank of size
\(C_{s-3}\) claimed in (0.1).  Each individual toggle is only an abstract
nonidentity-monodromy path-ledger switch.

#### Proof

For fixed \(R\), adjoining the common suffix state \(R\) to (5.2) uses
exactly the same set of local \(s\)-states as the canonical rank-three
prefix block: all \(A\cup R\), \(A\in\binom{[6]}3\).  Likewise (5.3)
uses all \(B\cup R\), \(B\in\binom{[6]}4\).  The local endpoint after
three Johnson steps is \(([6]\setminus P)\cup R\), exactly the canonical
boundary from which the unchanged suffix trace continues.  Therefore the
substitution preserves both global shores and every row's complementary
endpoint.

Different suffixes \(R\) give disjoint state and colour sets.  Thus all
substitutions commute and (6.2) is a vertex-disjoint bank.  Finally

\[
 \frac{C_{s-3}}{C_s}
 =\frac{s(s-1)(s+1)}
 {8(2s-1)(2s-3)(2s-5)}\longrightarrow\frac1{64}.      \tag{6.3}
\]

Each hexagon uses three roots, proving the second limit in (0.1).
\(\square\)

## 7. Exact boundary

The occurrence problem for alternating certificates is solved
existentially and refuted canonically: there is a positive-density
noncanonical host bank, while the canonical same-phase bank has size zero.
No positive physical twisted-slab claim survives Theorem 2.1.

The following stronger conclusions are not proved.

* The disjoint hexagons cannot be toggled independently inside an
  untwisted factor; their disjoint three-cycle monodromies remain.
* Three independent fixed-exterior twisted slabs are impossible, not
  merely unconstructed.  A surviving triple must be one jointly geodesic
  zero-monodromy phase packet, or must move the exterior according to
  (2.3) rowwise.
* No complete \(\mathcal D_s\)-port factor containing such a joint
  three-hexagon packet has been proved.
* The aggregate singleton carrier is zero, so a coefficient-one use must
  exploit row-dependent exteriors, the joint carrier (3.6), or deeper
  crossing windows.
* No favourable full background/capacity inequality follows merely from
  the positive occurrence density.

These are the precise remaining gates.
