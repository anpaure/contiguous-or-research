# Functional attachment after the reset: complete-host expansion, the root-coherence cut, and why protected owner exchange is static

Date: 2026-08-01

Status: unconditional complete-host expansion and exact Boolean exchange
obstructions, plus an authenticated `k=17` reset-extension census.  These
results do not construct the required one-flag-per-root exact selector.
They prove that the reset is harmless in the complete flexible host and
that the surviving obstruction is precisely the root-coherent correlated
rounding.

## 0. Outcome

At depth three the complete Boolean flag host has much more expansion than
the selected necklace table reveals.

Fix the one-coordinate rail state.  The bipartite graph between all tail
flag options and all head flag options is exactly

\[
                         (m+1)(m-2)\text{-regular}.             \tag{0.1}
\]

The finer graph from tail flags to aligned head--owner columns is
biregular with degrees

\[
                         (m+1)(m-2)\quad\text{and}\quad m-2,
                                                                  \tag{0.2}
\]

so every tail family expands by a factor at least `m+1` into columns.

For `k=17`, the normalized full flag graph has 80,080 vertices on each
shore, degree 54, and 4,324,320 edges.  Both the opened seven-edge reset
path and the closed eight-edge reset cycle extend to perfect matchings of
this full graph:

\[
                         80073/80073,qquad80072/80072.          \tag{0.3}
\]

Thus neither Boolean successor supply nor the reset bank is the problem.
The loss occurs when one projects to exactly one common flag per root.
That root-colour coherence can turn a 54-regular host into a table with
hundreds of universally dead tails.

Two proposed generic repairs do not cross this projection.

1. Rado's theorem selects representatives independent in one matroid.  Here
   the chosen columns must simultaneously be a head--owner matching and a
   predecessor transversal; the former is already an intersection of two
   partition matroids, not a matroid.
2. An owner-alternating exchange which preserves the current predecessor
   matching has no nonloop move in literal Boolean geometry.  At a matched
   tail--head pair the owner is forced to be their union.

The necessary move is therefore a simultaneous alternating circuit in the
full tail/head/owner hypergraph, together with a palette-neutral change of
the root flags.  Owner-only exchange cannot find it.

## 1. Exact depth-three predecessor sets

Put `k=2m+1`, `d=3`, and fix a shared rail coordinate `c`.  A normalized
tail flag has the unique form

\[
 f=(\{c\}\mathbin{\dot\cup}A\mathbin{\dot\cup}\{z\};z,c),
 \qquad |A|=m-2,                                      \tag{1.1}
\]

while a normalized head flag has the form

\[
 g=(\{c\}\mathbin{\dot\cup}H;c,\gamma),
 \qquad |H|=m-1,\quad\gamma\in H.                   \tag{1.2}
\]

Choose an aligned owner attachment at the head,

\[
                         o=q(g)\mathbin{\dot\cup}\{z\},       \tag{1.3}
\]

where `z` is outside the head root.  Then the complete-host predecessor
set of this column is

\[
 P_{\rm full}(g,o)=
 \left\{
   (\{c\}\cup(H-\{\beta\})\cup\{z\};z,c):
   \beta\in H-\{\gamma\}
 \right\}.                                             \tag{1.4}
\]

### Lemma 1.1 (punctured-facet formula)

Equation (1.4) is exact.  In particular,

\[
                         |P_{\rm full}(g,o)|=m-2.             \tag{1.5}
\]

#### Proof

The core form of a legal turn requires

\[
                         H=A\mathbin{\dot\cup}\{\beta\},
 \qquad \gamma\in A,\qquad z\ne\beta.               \tag{1.6}
\]

Since `z` lies outside the head, the last inequality is automatic.  The
condition `gamma in A` is equivalent to `beta != gamma`.  Solving (1.6)
for `A` gives (1.4), and its `m-2` choices are distinct. \(\square\)

Geometrically, all predecessors are facets of the one owner `o`.  Of its
`m+1` relevant rank-`m` facets, the three deletions at `c,z,gamma` are
forbidden and the remaining `m-2` are exactly (1.4).

For a **selected** table `F`, the actual predecessor set is simply

\[
 P_F(g,o)=\{f\in P_{\rm full}(g,o):
             \text{the flag }f\text{ was selected at its root}\}. \tag{1.7}
\]

This identity pinpoints the loss: owner choice can choose the punctured
facet star, but it cannot put a missing flag back at one of its roots.

## 2. Complete-host normalized matching

Let `L_c` contain every tail flag (1.1), and let `C_c` contain every aligned
head--owner column (1.2)--(1.3).  Join a tail to a column when it lies in
(1.4).

### Theorem 2.1 (factor-`m+1` column expansion)

This graph is biregular:

\[
 \deg_{L_c}=(m+1)(m-2),
 \qquad
 \deg_{C_c}=m-2.                                      \tag{2.1}
\]

Consequently every `X subseteq L_c` satisfies

\[
                         |N(X)|\ge(m+1)|X|.                   \tag{2.2}
\]

#### Proof

The right degree is Lemma 1.1.  For a tail `(c union A union z;z,c)`, choose
the entering coordinate `beta` outside its rank-`m` root in `m+1` ways and
the head refresh coordinate `gamma in A` in `m-2` ways.  This determines
one head flag and its owner column, proving the left degree.  Double-count
edges from `X` to `N(X)`:

\[
 (m+1)(m-2)|X|
 \le (m-2)|N(X)|.                                    \tag{2.3}
\]

Cancel `m-2`. \(\square\)

Collapse the `m+1` owner columns over one head flag.  A tail--head edge
determines its owner uniquely as the union of its roots.  The resulting
full flag-turn graph has degree `(m+1)(m-2)` on both shores.

### Corollary 2.2 (complete-host perfect matching)

The normalized full flag-turn graph has a perfect matching and satisfies
the normalized matching inequality

\[
                         |N(X)|\ge|X|.                         \tag{2.4}
\]

This theorem is before the one-flag-per-root equations.  A perfect matching
here uses **every flag option**, not one flag at every root, and therefore
is not the desired chronology.

## 3. Exact reset extension in the complete host

At `k=17,m=8`, normalize by the shared coordinate zero.  There are

\[
 \binom{16}{7}\cdot7=80080                             \tag{3.1}
\]

tail flags and the same number of head flags.  The degree from (0.1) is

\[
                         9\cdot6=54.                          \tag{3.2}
\]

### Theorem 3.1 (finite full-host reset extension)

The seven normalized edges of the opened rolling-reset path extend to a
perfect matching of the complete 80,080-by-80,080 flag graph.  So do all
eight edges of the closed reset ring.

#### Proof

The standalone audit constructs every normalized flag pair, all 4,324,320
legal edges using (1.6), verifies the protected reset edges literally,
deletes their endpoints, and runs exact Hopcroft--Karp.  The residual ranks
are (0.3). \(\square\)

This is finite evidence about the complete flexible host, not an
all-dimensional protected-extension theorem.  Its conceptual role is exact:
the reset is already compatible before root-colour coherence and exact
target marking are imposed.

## 4. Why Rado does not select `theta`

For one selected table, choosing a functional attachment and its predecessor
matching is the selection of triples

\[
                         (p,q,p\cup q)                        \tag{4.1}
\]

using every tail, head, and owner once.  Equivalently it is a rainbow
perfect matching in the legal tail--head graph, coloured by root union.

Rado's theorem applies to a family of sets with independence in one matroid.
Here the attachment columns must be independent simultaneously in:

* the head partition matroid;
* the owner partition matroid; and
* the predecessor transversal matroid.

Even the first two common bases are bipartite perfect matchings, whose edge
sets do not satisfy matroid basis exchange.  Hence there is no matroid to
which a black-box Rado theorem applies.

The complete-host expansion (2.2) proves the predecessor transversal has
enormous supply **before** root projection.  It supplies no rank inequality
for the intersection of the root-colour, head, owner, and predecessor rows.
The exact `k=17` selector from the independent quotient matchings proves
this sharply: it is rail-balanced and reset-compatible, yet has 406 tails
which are absent from every set (1.7).

## 5. Protected owner exchange has only loops

Fix a selected flag table, an owner transversal `D`, and a predecessor
matching `M` in `B_D`.  Suppose a matched edge uses tail `p`, head `q`, and
owner `o=D(q)`.

### Theorem 5.1 (Boolean union rigidity)

If another attachment column `a` at the same head `q` still admits the same
predecessor `p`, then

\[
                         o(a)=p\cup q=o.                       \tag{5.1}
\]

Therefore the `M`-protected owner-exchange multidigraph has no nonloop arc
through any matched head.  Parallel physical phases may give labelled
loops, but no owner reassignment.

#### Proof

Every literal rank-`m` turn has a unique rank-`m+1` owner, namely the union
of its two roots.  Both the current and alternative columns contain the
same literal turn `p -> q`, so both owners equal `p union q`. \(\square\)

### Corollary 5.2 (owner-only augmentation no-go)

The protected attachment-cycle augmentation theorem cannot use a nontrivial
return path while preserving every edge of `M`.  It can improve `M` only
when an unmatched head has a different physical phase of its **currently
assigned owner** which directly sees the alternating reachable tail shore.

Any augmentation which genuinely changes the owner assignment must reroute
some predecessor edges at the same time.  Its primitive is an alternating
circuit in the full tripartite turn hypergraph, not an owner cycle with `M`
frozen.

This explains why the reset-conditioned problem remains a three-resource
matching despite the exact owner-transversal extension theorem.

## 6. The smallest literal Hall obstruction

For a selected depth-three table, write a tail as in (1.1).  Its possible
successor roots are

\[
 q_\beta=\{c\}\cup A\cup\{\beta\},
 \qquad \beta\notin q(f).                              \tag{6.1}
\]

### Proposition 6.1 (dead-tail criterion)

The tail `f=(c union A union z;z,c)` has some legal successor under some
owner attachment if and only if, for at least one `beta` outside its root,
the selected flag at `q_beta` is

\[
                         (q_\beta;c,\gamma)
                         \quad\text{with }\gamma\in A.        \tag{6.2}
\]

#### Proof

This is (1.6), with the owner then forced to be `q_beta union {z}`. \(\square\)

The criterion gives a singleton Hall cut.  No choice of `theta` can repair
its failure.

### Proposition 6.2 (minimum-dimensional literal example)

Depth three first exists at `m=3,k=7`.  The exact recursive-SCD selector
contains

\[
 p=\{0,1,6\},\qquad f_p=(p;1,0),\qquad A=\{6\}.       \tag{6.3}
\]

Its possible successor roots are

\[
 q_\beta=\{0,6,\beta\},\qquad\beta\in\{2,3,4,5\},   \tag{6.4}
\]

but the selected flag at each is

\[
                         (q_\beta;0,\beta).                   \tag{6.5}
\]

Since `beta notin A`, equation (6.2) fails four times.  Thus `p` is
universally dead.  This is the smallest possible dimension for a literal
depth-three dead-tail obstruction.

That table is not rail-balanced.  Inside the relevant rail-balanced,
reset-conditioned face, the authenticated `k=17` independent completion is
the current literal witness: 406 universal dead tails and residual state
matching rank `850/1423` after opening the reset.

There is a separate fractional warning.  Physical Boolean turn geometry
forbids the generic strong `C3`, but admits a clean strong `C5`; the
authenticated GKS `k=17` table contains a zero-holonomy example.  Hence even
after singleton Hall cuts are removed, balanced-matrix/TU rounding is not
automatic.  `C5` is the smallest literal strong odd-cycle obstruction.

## 7. What remains possible

The negative results do not refute a jointly designed `theta`.  They say
exactly what a positive theorem must do.

1. Select one flag per root while preserving a positive fraction of the
   complete-host expansion (2.2).
2. Select a rainbow tail--head perfect matching at the same time; its owner
   map is then forced by union.
3. Use alternating circuits that reroute tail, head, and owner assignments
   simultaneously.
4. Preserve the two quotient target matchings and the opened reset path.

A sufficient robust theorem would be a root-coherent version of (2.2): for
every residual tail family `X`, the jointly available head--owner columns
must contain `|X|` columns with distinct heads and owners.  That is already
the exact three-matroid rank inequality; ordinary normalized matching or
Rado cannot prove it after the root-colour projection.

## 8. Audit artifacts

The complete-host reset replay is

`scratch/audit_k17_full_flag_host_reset_extension_20260801.cpp`

with frozen output

`scratch/audit_k17_full_flag_host_reset_extension_20260801.txt`.

It was compiled with `-O3` and run on the H100 CPU.  The selected-table
audit remains

`scratch/audit_k17_necklace_selector_reset_bank_20260801.cpp`.

The distinction between the two artifacts is intentional:

* the first proves the reset extends in the complete flexible flag host;
* the second proves one exact root-coherent selector can still fail at a
  singleton Hall cut.

SHA-256 of the complete-host source/output:

* `95147c5b5b863c4124c06cf70669bc2d94400fa31194008ec8bab05e6bc0cec4`;
* `7df38c16d545258febecd57000a9493691aa1d39188b1d411bb7ba3d7cc0337a`.
