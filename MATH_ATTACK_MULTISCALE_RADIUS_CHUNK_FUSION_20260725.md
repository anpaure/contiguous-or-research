# Multiscale radius chunks: the reset theorem and the history obstruction

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

Put

\[
 W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.                  \tag{0.1}
\]

Fix a controlled depth \(Q=o(m)\).  The unique truncated symmetric-chain
radius law is

\[
 c_d=N_d-N_{d+1}\quad(0\le d<Q),\qquad c_Q=N_Q,
 \qquad \sum_{d=q}^Q c_d=N_q.                          \tag{0.2}
\]

This note proves two complementary statements.

1. **Reset-positive theorem.**  Suppose radius-\(d\) owners are organized
   into buffered chunks of common central length at least \(\ell\), apart
   from one remainder chunk at each radius, and their counts are exactly
   \(c_d\).  Compiling the radii separately costs at most

   \[
   \boxed{
   R_{\rm sep}
   \le {W+2\sum_{q=1}^Q N_q\over\ell}+O(Q^2)
   =O\!\left({W\sqrt m\over\ell}+Q^2\right).}
   \tag{0.3}
   \]

   Hence \(\ell/\sqrt m\to\infty\) gives \(R_{\rm sep}=o(W)\), even when
   \(\ell=o(Q)\).  Cross-radius sharing of resets is unnecessary.  More
   generally, radius-dependent chunk lengths \(\ell_d\) work under the
   weighted sufficient condition

   \[
   \sum_{d=0}^Q{(2d+1)c_d\over\ell_d}=o(W).             \tag{0.4}
   \]

2. **Immutable-history obstruction.**  Owner-near-perfect chunk systems
   at several radii do not automatically fuse.  If their prescribed first
   transitions give \(a(X)\) distinct successors to owner \(X\), every
   fusion which preserves those chunk histories needs at least

   \[
   \boxed{
   |\mathcal O|+\sum_{X\in\mathcal O}(a(X)-1)_+}
   \tag{0.5}
   \]

   certified owner starts.  Thus successor disagreement on
   \(\delta W\) owners forces \(\delta W\) excess length.  Marginal
   near-perfectness at each radius contains no bound on (0.5).

There is a sharp positive fusion criterion between these statements.  If
the selected radius chunks are subchunks of one near-spanning directed
linear forest, their higher histories agree, their radius flags have only
\(o(W)\) total duplicate excess, and the weighted reset ledger is \(o(W)\),
then they compile to one nonzero contiguous-OR word of length \(W+o(W)\)
covering every rank \(m-q,\ldots,m+q\), \(q\le Q\).  If the two binomial
tails outside this band have size \(o(W)\), this is a coefficient-one word.

The conclusion is therefore precise: short multiradius chunks can pay
\(o(W)\) resets.  The unresolved theorem is an integral, history-compatible
selection of the chunks with \(o(W)\) shadow collisions.  Independent
owner-near-perfect supplies at the separate radii do not supply that
correlation.

## 1. The forced radius distribution

A radius-\(d\) central start supplies one mask in each of the ranks

\[
 m-d,m-d+1,\ldots,m+d.                                \tag{1.1}
\]

Let \(s_d\) be the number of selected starts assigned exact radius \(d\).
The number of available flag occurrences at either depth \(q\) is

\[
 T_q=\sum_{d=q}^Q s_d.                                 \tag{1.2}
\]

If every band mask is covered exactly once, then \(T_q=N_q\).  Backward
differencing forces

\[
 s_d=N_d-N_{d+1}\quad(d<Q),\qquad s_Q=N_Q.             \tag{1.3}
\]

Thus (0.2) is not an arbitrary convenient mixture.  It is the only radius
mixture compatible with exact rank-by-rank capacity.

For approximate coverage, write

\[
 e_d=s_d-c_d,\qquad
 A_Q=\sum_{q=0}^Q\left|\sum_{d=q}^Qe_d\right|.          \tag{1.4}
\]

The quantity \(A_Q\), not merely \(\sum_d|e_d|\), is the correct aggregate
rank-supply error.  Indeed,

\[
 T_q-N_q=\sum_{d=q}^Qe_d.                              \tag{1.5}
\]

The exact size of one radius class is

\[
 c_d=N_d{2d+1\over m+d+1}\qquad(d<Q),                 \tag{1.6}
\]

because

\[
 {N_{d+1}\over N_d}={m-d\over m+d+1}.                  \tag{1.7}
\]

Thus the radius of a uniformly chosen middle member has a Rayleigh-scale
distribution: most of its mass lies at \(d=\Theta(\sqrt m)\), regardless
of a larger truncation depth \(Q\).

The exact first moment is especially useful.

### Lemma 1.1 (radius-mass identity)

\[
 \boxed{
 \sum_{d=0}^Q d\,c_d=\sum_{q=1}^Q N_q.}
 \tag{1.8}
\]

#### Proof

Using \(c_d=N_d-N_{d+1}\) for \(d<Q\) and \(c_Q=N_Q\),

\[
 \begin{aligned}
 \sum_{d=0}^Qd\,c_d
 &=\sum_{d=0}^{Q-1}d(N_d-N_{d+1})+QN_Q\\
 &=N_1+N_2+\cdots+N_Q.
 \end{aligned}
\]

This is ordinary summation by parts. \(\square\)

There is an elementary uniform Gaussian upper bound.  For \(q\le m\),

\[
 {N_q\over W}
 =\prod_{i=0}^{q-1}{m-i\over m+i+1}
 \le\exp\!\left(-{q^2\over2m}\right).                  \tag{1.9}
\]

Indeed,

\[
 {m-i\over m+i+1}
 =1-{2i+1\over m+i+1}
 \le\exp\!\left(-{2i+1\over2m}\right),
\]

and \(\sum_{i<q}(2i+1)=q^2\).  Consequently

\[
 \sum_{q=1}^Q N_q=O(W\sqrt m).                        \tag{1.10}
\]

For \(Q/\sqrt m\to\infty\), the sharper standard central expansion gives

\[
 {1\over W}\sum_{q=1}^Q N_q
 =\left({\sqrt\pi\over2}+o(1)\right)\sqrt m,            \tag{1.11}
\]

but the upper bound (1.10) is all that the reset theorem needs.

## 2. Buffered chunks and their literal cost

Let

\[
 X_{-d},X_{-d+1},\ldots,X_{\ell+d}
 \in\binom{[2m]}m                                      \tag{2.1}
\]

be a Johnson walk, and suppose the transition supports in the displayed
interval are pairwise disjoint.  The central starts are
\(X_0,\ldots,X_{\ell-1}\).  For \(0\le q\le d\), put

\[
 L_q(i)=\bigcap_{j=0}^qX_{i+j},\qquad
 U_q(i)=\bigcup_{j=0}^qX_{i-j}.                        \tag{2.2}
\]

Support separation gives

\[
 |L_q(i)|=m-q,\qquad |U_q(i)|=m+q,                     \tag{2.3}
\]

and

\[
 L_d(i)\subset\cdots\subset L_1(i)\subset X_i
 \subset U_1(i)\subset\cdots\subset U_d(i).            \tag{2.4}
\]

Call (2.1) a buffered radius-\(d\) chunk of central length \(\ell\).

### Lemma 2.1 (literal chunk compiler)

A buffered radius-\(d\) chunk with \(\ell\) central starts has a genuine
nonzero contiguous-OR word of length at most

\[
 \boxed{\ell+2d+1}                                     \tag{2.5}
\]

which exposes every mask in (2.4), for every central start.  If a start is
assigned a smaller radius, truncating its chain costs no additional letter.

#### Proof

Write the transition \(X_{i+1}=X_i-p_i+u_i\).  Support separation makes the
next \(d\) departures and the previous \(d\) departures pairwise distinct.
At the first central start initialize the ordered MTF state

\[
 \bigl(
 L_d(0),\{p_{d-1}\},\ldots,\{p_0\},
 \{p_{-1}\},\ldots,\{p_{-d}\},\mathcal R
 \bigr),                                               \tag{2.6}
\]

where \(\mathcal R\) is the residual block.  Its successive prefix unions
are the lower and upper members of (2.4).  The first central chain costs at
most \(2d+2\) nonempty state entries.  Appending the next lower core performs
the next MTF update, so each of the remaining \(\ell-1\) central starts
costs one entry.  The total is
\((2d+2)+(\ell-1)=\ell+2d+1\).  Omitting outer prefix unions merely
truncates the exposed chain and changes no letter. \(\square\)

For a collection of chunks, let \(J_d\) be the number of exact-radius-\(d\)
chunks and \(s_d\) their total number of central starts.  Concatenation gives
the reset/initialization ledger

\[
 R_{\rm sep}\le\sum_{d=0}^Q(2d+1)J_d.                  \tag{2.7}
\]

No shadow-disjointness assumption is used in (2.7).

## 3. The multiscale reset theorem

### Theorem 3.1 (radius-dependent chunk lengths)

Suppose that, for every \(d\), all but at most one radius-\(d\) chunk have
central length at least \(\ell_d\).  Then

\[
 J_d\le {s_d\over\ell_d}+1                             \tag{3.1}
\]

and hence

\[
 \boxed{
 R_{\rm sep}
 \le\sum_{d=0}^Q{(2d+1)s_d\over\ell_d}+O(Q^2).}
 \tag{3.2}
\]

In particular, if \(s_d=c_d+e_d\), the conditions

\[
 \sum_{d=0}^Q{(2d+1)c_d\over\ell_d}=o(W),\qquad
 \sum_{d=0}^Q{(2d+1)|e_d|\over\ell_d}=o(W)             \tag{3.3}
\]

imply \(R_{\rm sep}=o(W)\).

#### Proof

At most \(s_d/\ell_d\) chunks can have length at least \(\ell_d\), plus the
one allowed remainder.  Substitute (3.1) in (2.7).  Since

\[
 \sum_{d=0}^Q(2d+1)=O(Q^2)=o(W),                       \tag{3.4}
\]

the result follows. \(\square\)

The phrase “short chunks” therefore has a precise threshold.  A sufficient
uniform condition is

\[
 \ell_d\ge\omega_m(2d+1),\qquad \omega_m\to\infty,     \tag{3.5}
\]

which makes the first sum in (3.3) at most \(W/\omega_m\).  This still
allows \(\ell_d=o(m)\) for every \(d\le Q=o(m)\).

There is a stronger uniform-length consequence which uses the actual radius
distribution.

### Corollary 3.2 (common short length)

If \(s_d=c_d\) and every radius uses chunks of central length at least
\(\ell\), apart from one remainder per radius, then

\[
 \begin{aligned}
 R_{\rm sep}
 &\le {1\over\ell}\sum_{d=0}^Q(2d+1)c_d+O(Q^2)\\
 &={W+2\sum_{q=1}^QN_q\over\ell}+O(Q^2)\\
 &=O\!\left({W\sqrt m\over\ell}+Q^2\right).
 \end{aligned}                                         \tag{3.6}
\]

Hence

\[
 {\ell\over\sqrt m}\longrightarrow\infty
 \quad\Longrightarrow\quad R_{\rm sep}=o(W).           \tag{3.7}
\]

For \(Q\asymp\sqrt{m\log m}\), one may choose

\[
 \sqrt m\ll\ell\ll Q.                                  \tag{3.8}
\]

Thus the central pieces can be shorter than the largest radius and still
have negligible **total**, not merely per-radius, reset cost.  The reason is
that only the \(N_Q\) tail owners reach the largest radius.

This proves the reset portion of multiscale lifting.  Any further fusion of
different radii onto common chunks can improve (3.6), but is not needed for
coefficient one.

## 4. Exact shadow-defect accounting

For a chosen multiradius chunk family, let

\[
 V_0=\#\{\text{distinct middle owners}\},\qquad
 C_0=\sum_{d=0}^Qs_d-V_0.                              \tag{4.1}
\]

Thus \(C_0\) is the middle duplicate excess.  Put

\[
 h_0=W-V_0=W-\sum_ds_d+C_0.                            \tag{4.2}
\]

For \(q\ge1\) and sign \(\sigma\in\{-,+\}\), let
\(V_q^\sigma\) be the number of distinct masks among the selected
depth-\(q\) flags.  Define

\[
 D_q^\sigma=T_q-V_q^\sigma,\qquad
 h_q^\sigma=N_q-V_q^\sigma.                            \tag{4.3}
\]

Then the exact identity is

\[
 \boxed{
 h_q^\sigma=N_q-T_q+D_q^\sigma.}
 \tag{4.4}
\]

Consequently,

\[
 \sum_{q=1}^Q(h_q^-+h_q^+)
 \le 2A_Q+\sum_{q=1}^Q(D_q^-+D_q^+).                  \tag{4.5}
\]

No marginal probabilities have been multiplied: (4.4) is an identity in
the selected joint chunk family.

### Theorem 4.1 (multiscale chunk sufficient theorem)

Assume a family of buffered radius chunks satisfies

\[
 \left|\sum_ds_d-W\right|+C_0=o(W),                   \tag{4.6}
\]

\[
 A_Q+\sum_{q=1}^Q(D_q^-+D_q^+)=o(W),                  \tag{4.7}
\]

and

\[
 \sum_{d=0}^Q(2d+1)J_d=o(W).                          \tag{4.8}
\]

Then there is a nonzero contiguous-OR word of length \(W+o(W)\) covering
every selected middle owner and every selected flag, and after literal
repair it covers every mask in the central band

\[
 m-Q,m-Q+1,\ldots,m+Q.                                \tag{4.9}
\]

If the number of Boolean masks outside this band is \(o(W)\), appending
those masks gives a universal word of length \(W+o(W)\).

#### Proof

Compile and concatenate all chunks using Lemma 2.1.  Their total length is
at most

\[
 \sum_ds_d+\sum_d(2d+1)J_d.                            \tag{4.10}
\]

Append the \(h_0\) missing middle masks.  By (4.2), the central-start terms
plus this repair equal

\[
 \sum_ds_d+h_0=W+C_0.                                  \tag{4.11}
\]

Append all missing shadow masks.  Their total number is \(o(W)\) by
(4.5) and (4.7).  Finally use (4.8).  The resulting length is

\[
 W+C_0+o(W)=W+o(W).                                    \tag{4.12}
\]

All appended masks are nonempty.  If the outer tails have size \(o(W)\),
append them as well. \(\square\)

Combining Theorem 4.1 with Corollary 3.2 shows that the reset requirement
is already solved by exact-radius chunks of common length
\(\ell\gg\sqrt m\).  The only nonformal hypotheses left are the joint owner
and flag collision bounds (4.6)--(4.7).

## 5. Common-backbone fusion

Several radii may be placed on one physical chunk.  Let a central start
\(X_i\) be assigned a radius \(d_i\le D\).  Lemma 2.1 compiles the entire
variable-radius chunk in

\[
 \ell+2D+1                                             \tag{5.1}
\]

letters: construct the radius-\(D\) state and retain only the flags through
depth \(d_i\) at start \(i\).

This observation extends to a family of already selected chunks.

### Theorem 5.1 (immutable common-backbone fusion)

Suppose a collection of radius-labelled chunks has the following
properties after deleting \(b\) certified starts.

1. The union of all prescribed directed middle transitions has indegree and
   outdegree at most one at every remaining owner.
2. Every resulting component is a directed path or directed cycle, and
   every retained radius-\(d\) start has its prescribed \(d\)-step past and
   future inside that component.
3. Those \(2d\) transitions are support-separated for every retained start.

Cut one edge in each directed cycle.  If the resulting path components are
\(\mathcal P\), and \(D(P)\) is the largest radius assigned to a start on
\(P\), then all retained chunks fuse without changing any of their flags
into words of total length at most

\[
 \boxed{
 S-b+\sum_{P\in\mathcal P}(2D(P)+1),}
 \tag{5.2}
\]

where \(S=\sum_ds_d\) is the original number of certified starts.

#### Proof

The degree condition makes every component a directed path or cycle.
After one cut per cycle, all prescribed transitions occur in the resulting
path order.  Conditions 2--3 say that every prescribed flag is exactly the
corresponding consecutive intersection or union window of that common path.
Apply the variable-radius form of Lemma 2.1 to each component.  No flag is
changed, and summing (5.1) gives (5.2). \(\square\)

Thus a genuine cross-radius fusion theorem consists of two independent
parts:

\[
 b=o(W),\qquad
 \sum_{P\in\mathcal P}(2D(P)+1)=o(W).                  \tag{5.3}
\]

When these hold, the reset ledger is smaller than (3.2).  The theorem also
shows exactly what “compatible chunks” means: they must be restrictions of
one radius-labelled linear forest, not merely near-perfect marginal
packings on the same owner set.

## 6. The immutable-history lower bound

Let \(\mathcal F_1,\ldots,\mathcal F_k\) be directed chunk forests on owner
sets contained in a common set \(\mathcal O\).  Retain all their prescribed
first transitions.  For \(X\in\mathcal O\), put

\[
 \Gamma^+(X)
 =\{Y:X\longrightarrow Y
       \text{ is prescribed by at least one }\mathcal F_i\},
 \qquad a(X)=|\Gamma^+(X)|.                            \tag{6.1}
\]

An **immutable fusion** is any collection of directed start sequences which
contains every owner in \(\mathcal O\) at least once and contains every
prescribed edge \(X\to Y\) as two consecutive certified starts.  Owners may
be repeated.

### Theorem 6.1 (successor-disagreement obstruction)

Every immutable fusion has at least

\[
 \boxed{
 |\mathcal O|+\sum_{X\in\mathcal O}(a(X)-1)_+}
 \tag{6.2}
\]

certified starts.

The analogous lower bound holds with distinct predecessors in place of
successors.

#### Proof

One occurrence of a certified start labelled \(X\) has at most one immediate
successor.  Therefore the \(a(X)\) distinct prescribed successors require at
least \(a(X)\) occurrences of \(X\).  If \(a(X)=0\), representing the owner
itself still requires one occurrence.  Hence the multiplicity of \(X\) is at
least \(\max\{1,a(X)\}=1+(a(X)-1)_+\).  Sum over \(X\). \(\square\)

### Corollary 6.2 (linear disagreement forbids coefficient one)

Suppose \(|\mathcal O|=W-o(W)\) and

\[
 \Delta^+
 :=\sum_{X\in\mathcal O}(a(X)-1)_+
 \ge\delta W                                           \tag{6.3}
\]

for some fixed \(\delta>0\).  Every immutable fusion has at least

\[
 (1+\delta-o(1))W                                      \tag{6.4}
\]

certified starts, before any reset or shadow repair is paid.

In particular, if two owner-near-perfect radius systems prescribe different
successors on \(\delta W\) common owners, they cannot be fused at coefficient
one while retaining their chosen chunks.

This obstruction is deliberately scoped.  It does not rule out discarding
and recoding a linear number of transitions while preserving the shadows by
different witnesses.  It proves that no theorem based only on marginal
owner-near-perfectness can justify fusion of the **given** chunks.  Such a
theorem must either prove \(\Delta^+=o(W)\), construct a common backbone
from the outset, or supply a non-immutable recoding of the shadow witnesses.

## 7. Consequences for a multiscale attack

The radius-by-radius plan now has an exact ledger.

1. Extract approximately \(c_d\), not \(W\), owners at exact radius \(d\).
   Using an owner-near-perfect family at every radius without thinning would
   spend one width baseline per radius.
2. Chunks of common length \(\ell\gg\sqrt m\) make the sum of all reset
   costs \(o(W)\), by (3.6).  It is unnecessary to demand
   \(\ell\gg Q\).
3. The tail supply discrepancies must obey \(A_Q=o(W)\).  Separate
   per-radius estimates cannot be summed without this check.
4. The actual cross-radius shadow duplicate excess in (4.7) must be
   \(o(W)\).  Multiplication of marginal coverage probabilities is
   irrelevant.
5. If the chosen chunk histories are retained, their successor and
   predecessor disagreement masses must be \(o(W)\), by Theorem 6.1.
6. A common-backbone selection satisfying these joint conditions gives the
   desired word by Theorems 4.1 and 5.1.

For the standard tail depth

\[
 Q=(1+\eta)\sqrt{m\log m}\qquad(\eta>0),               \tag{7.1}
\]

the number of masks outside the central band is \(o(W)\).  Hence the common
backbone theorem at this \(Q\), together with any
\(\sqrt m\ll\ell=o(m)\) satisfying the support-separation requirement, is a
complete coefficient-one sufficient condition.

## 8. Audit ledger

### Proved

1. The forced radius law is (0.2), with exact class sizes (1.6).
2. The radius first moment is \(\sum d c_d=\sum_{q\le Q}N_q=O(W\sqrt m)\).
3. Buffered radius-\(d\) chunks compile in \(\ell+2d+1\) letters.
4. The exact separate-radius reset bound is (3.2).
5. Common length \(\ell\gg\sqrt m\) gives total reset \(o(W)\), even when
   \(\ell=o(Q)\).
6. The exact shadow hole/duplicate identity is (4.4).
7. The joint conditions (4.6)--(4.8) imply a \(W+o(W)\) central-band word.
8. Compatible multiradius chunks fuse on a common backbone with cost (5.2).
9. Successor disagreement forces the owner-occurrence lower bound (6.2).

### Still open

1. Near-perfect owner chunk packings at separate radii are not proved to
   admit an extraction with \(A_Q=o(W)\).
2. Their cross-radius shadow duplicate excess is not proved to be \(o(W)\).
3. Their successor/predecessor disagreement is not proved to be \(o(W)\).
4. No non-immutable recoding theorem bypassing Theorem 6.1 is proved.
5. Therefore the reset problem is solved, but the integral common-backbone
   and shadow-incidence theorem required for coefficient one remains open.
