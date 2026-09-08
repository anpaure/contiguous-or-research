# Context-dependent macro-order arrays on the canonical packet union

## Status

The fixed round-robin macro-order is genuinely dead: at Gaussian depth it
forces a long run of target-ineligible physical blocks.  That obstruction is
not an obstruction to the tensor packet itself.  The product decomposition
contains exponentially many disjoint cube cells, and the direction order may
be chosen independently in every cell without disturbing exact ownership.

This note proves three unconditional facts.

1. A packet admits at least
   \[
     \left({(2r)!\over 2^r}\right)^{6^r}
   \]
   independently prescribed directed macro-order fields.
2. There is one such field in which, simultaneously for every
   \(q\le H=o(r)\), every \(q\)-subset of the \(r\) macroblocks occurs as a
   consecutive-window support the same number of times up to relative
   \(o(1)\).
3. Consequently the fixed-order support obstruction disappears completely at
   the cell-catalogue level: the depth-\(q\) macro-support census is
   asymptotically uniform over all \(\binom rq\) supports.

The result does **not** yet prove literal target coverage.  It supplies the
previously missing macro-support menu; the remaining issue is routing physical
targets to compatible source cells and controlling collisions between those
routes.

## 1. Setup

Fix one canonical tensor packet with \(r\) selected eight-blocks.  Fix one of
the two local pair-frame choices in every block.  The local product theorem
partitions the packet into

\[
                        N=6^r                                      \tag{1.1}
\]

pairwise disjoint cells, every one isometric to \(Q_{2r}\).  Write the two
cube directions belonging to macroblock \(i\) as

\[
                         \alpha_i,\ \beta_i,
                         \qquad i\in[r].                            \tag{1.2}
\]

Assume \(2r\) is a power of two, so a fixed Hamming resolution class gives an
exact \(C_{4r}\)-factor of every cell.  Conjugating this factor by any
coordinate permutation of \(Q_{2r}\) gives another exact factor of that cell.

## 2. Independent-cell conjugation

### Theorem 2.1 (context-dependent exact factor)

For every function

\[
 \Sigma:\{\text{the }6^r\text{ cells}\}\longrightarrow S_{2r},    \tag{2.1}
\]

conjugate the fixed Hamming factor in cell \(K\) by \(\Sigma(K)\).  The union
of the resulting cell factors is an exact \(C_{4r}\)-factor of the entire
packet.

#### Proof

Coordinate conjugation is a cube automorphism, so it maps an exact factor of
one cell to an exact factor of that same cell.  The \(6^r\) cells are disjoint
and exhaust the packet.  Hence choices in distinct cells are independent and
their union partitions every owner once. \(\square\)

Thus the macro-order can depend arbitrarily on the full cell label
\((j_1,\ldots,j_r)\in[6]^r\), which is precisely an outside-context-dependent
order field.

## 3. Exact order capacity

Forget the distinction between \(\alpha_i\) and \(\beta_i\), retaining only
their common macroblock label \(i\).  A coordinate permutation produces a word
of length \(2r\) containing each label twice.  Conversely every such word is
realized: assign its first occurrence of \(i\) to \(\alpha_i\) and its second
to \(\beta_i\).

### Theorem 3.1 (number of realizable macro-order fields)

The number of distinct directed macro words available in one cell is exactly

\[
                         M_r={ (2r)!\over 2^r}.                     \tag{3.1}
\]

Consequently the number of independently realizable directed macro-order
fields on one packet is exactly

\[
                         M_r^{,6^r}.                              \tag{3.2}
\]

If cyclic rotation and reversal are identified, the number of geometric
fields lies between

\[
 \left({M_r\over4r}\right)^{6^r}
 \quad\hbox{and}\quad
 M_r^{6^r}.                                                        \tag{3.3}
\]

#### Proof

There are \((2r)!\) physical direction permutations.  Swapping
\(\alpha_i\) and \(\beta_i\) independently for the \(r\) labels leaves the
macro word unchanged, and these \(2^r\) permutations are the complete fibre
over a macro word.  This proves (3.1).  Theorem 2.1 makes the choices in the
\(6^r\) cells independent, proving (3.2).  A directed word has at most
\(2r\) rotations and two orientations, proving (3.3). \(\square\)

In logarithmic form,

\[
 \log \#\{\text{fields}\}
 =6^r\big(2r\log(2r)-2r-r\log2+O(\log r)\big),                    \tag{3.4}
\]

so this is doubly exponential in the context length \(r\) and is not an
entropy-starved catalogue.

## 4. A balanced permutation array

For the support theorem it suffices to use the much smaller separated family

\[
 \sigma_\pi=
 (\alpha_{\pi_1},\ldots,\alpha_{\pi_r},
  \beta_{\pi_1},\ldots,\beta_{\pi_r}),
 \qquad \pi\in S_r.                                               \tag{4.1}
\]

Its macro word is \(\pi\pi\).  If \(q<r\), a length-\(q\) direction window
therefore has macro support equal to a cyclic length-\(q\) interval of
\(\pi\), and every such interval occurs four times during the full
length-\(4r\) Hamming cycle.

For a cell array \(\Pi=(\pi_K)_{K\in[6]^r}\), let

\[
 X_{q,J}(\Pi)=
 \#\{K:J\text{ is a cyclic }q\text{-interval of }\pi_K\},
 \qquad J\in\binom{[r]}q.                                        \tag{4.2}
\]

### Theorem 4.1 (simultaneous balanced support array)

Let \(H=H(r)=o(r)\).  There is an array \(\Pi\in(S_r)^{6^r}\) such that,
simultaneously for all \(1\le q\le H\) and all
\(J\in\binom{[r]}q\),

\[
 X_{q,J}(\Pi)
 =\left(1+o(1)\right){6^r r\over\binom rq},                      \tag{4.3}
\]

where the error is uniform in \(q,J\).

#### Proof

Choose the \(6^r\) permutations independently and uniformly from \(S_r\).
For fixed \((q,J)\), symmetry and double counting of the \(r\) cyclic
intervals give

\[
 \Pr(J\text{ is a cyclic }q\text{-interval})={r\over\binom rq}.  \tag{4.4}
\]

Thus \(X_{q,J}\) is binomial with mean

\[
 \mu_{q,J}={6^r r\over\binom rq}.                                \tag{4.5}
\]

Because \(H=o(r)\),

\[
 \log\sum_{q\le H}\binom rq=o(r),                               \tag{4.6}
\]

whereas uniformly on this range

\[
 \log \mu_{q,J}=r\log6-o(r).                                    \tag{4.7}
\]

Take any \(\delta_r\downarrow0\) slowly, for example
\(\delta_r=r^{-1}\).  Chernoff gives

\[
 \Pr\big(|X_{q,J}-\mu_{q,J}|>\delta_r\mu_{q,J}\big)
 \le2\exp(-\delta_r^2\mu_{q,J}/3).                              \tag{4.8}
\]

The union bound over (4.6) tends to zero super-exponentially.  Hence an array
with (4.3) exists. \(\square\)

### Corollary 4.2 (uniform owner-start census)

Use the exact factor from Theorem 2.1 with the orders (4.1) supplied by an
array from Theorem 4.1.  Let \(L_{q,J}\) be the number of owner starts in the
packet whose next \(q\) deletions use precisely the macroblocks in \(J\).
Then, simultaneously for \(q\le H\),

\[
 L_{q,J}
 =\left(1+o(1)\right){24^r\over\binom rq}.                       \tag{4.9}
\]

#### Proof

One cell contains \(2^{2r}/(4r)\) cycles.  If \(J\) is a cyclic interval of
its permutation, it occurs at four starts per cycle, hence contributes

\[
 {2^{2r}\over r}                                                 \tag{4.10}
\]

owner starts.  Multiply (4.10) by (4.3), and use
\(6^r2^{2r}=24^r\). \(\square\)

Thus the macro-support projection is as balanced as it can be: every
\(q\)-subset receives its exact average up to relative \(o(1)\).  In
particular, for each \(q\le H\), **every** macro support occurs exponentially
many times.  The long ineligible-run theorem for one fixed order has no
analogue for this context-dependent atlas.

## 5. Deterministic covering with far fewer order types

The probabilistic balancing is stronger than mere support coverage.  Since

\[
 \sum_{q\le H}\binom rq=\exp(o(r))\ll6^r,                         \tag{5.1}
\]

one may instead assign a separate cell to every pair \((q,J)\), choose a
permutation in which \(J\) is consecutive, and fill all unused cells
arbitrarily.  Hence every shallow support can be forced even without
concentration.  Theorem 4.1 shows that the exponential surplus of cells is
large enough to equalize the full census, not just to hit each support once.

## 6. What remains

The fixed-order obstruction has now been removed at exactly the level where it
arose.  The following implications are **not** proved by this note.

1. A macro support \(J\) does not by itself identify a literal
   rank-\((m-q)\) target.  One must prove that enough compatible source cells
   feed every physical target.
2. The Hamming factor may have literal face collisions even when the projected
   macro-support census is uniform.  A face-simple local factor or a separate
   collision ledger is still required.
3. The canonical packet union omits an exponentially small owner leave.  In a
   simultaneous \(H\)-depth estimate the leave is charged \(H\) times; the
   canonical exponential leave remains negligible, but an arbitrary
   \(o(W)\) leave would not suffice.
4. The cell-wise permutations above depend on the source cell label.  The
   remaining theorem is therefore a cross-cell transportation statement, not
   another direction-order existence statement.

The exact surviving gate can be stated cleanly: prove that the balanced array
of Corollary 4.2 can be chosen so that its literal target map has total
collision excess \(o(W)\) (or missing mass \(o(W)\)) simultaneously over the
mesoscopic depths.  The previous fixed-order support deficit contributes zero
to that gate.

## 7. Verdict

Allowing the direction order to depend on the product-cell context changes the
picture decisively.  There are \(((2r)!/2^r)^{6^r}\) realizable macro-order
fields, and a simple permutation-array argument produces an exact owner factor
whose shallow macro-support histogram is asymptotically uniform at every depth
\(q\le o(r)\).  Hence the fixed round-robin failure is not a packet-capacity
no-go.  What remains is literal cross-cell target routing and collision
control.
