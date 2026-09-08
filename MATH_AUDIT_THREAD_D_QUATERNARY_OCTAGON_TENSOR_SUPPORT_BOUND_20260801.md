# The quaternary octagon has a sharp `8d+23` resident tensor floor

Date: 2026-08-01  
Lane: Thread D, local nonflat replacement for the two-star obstruction  
Status: exact theorem inside the one-block-per-port coatom tensor template.
It proves neither a literal four-source-star inverse nor a global host.

## 0. Verdict

The quaternary octagon does remove the **owner-rank** obstruction of the
asymmetric two-star packet.  Its two phases admit two rank-two Hamilton
paths on the same eight active ports, with four changed octagon edges and
three common connector edges.  However the unexpanded paths have internal
coordinate runs of length one, so they are not depth-`d` resident.

There is a sharp resident repair in the natural coatom tensor.  Replace
each active port by an `n`-coatom block and each of the seven path edges by
one rank-preserving screen.  The screen pattern is

\[
                         I,U,I,U,I,U,I .                 \tag{0.1}
\]

At every union screen an endpoint filler has an internal positive run of
length exactly `n-1`.  Therefore depth-`d` residence forces

\[
                              n\ge d+2.                   \tag{0.2}
\]

Conversely `n=d+2` works exactly.  Since the support-four absorber has
eight distinct ports and a path through eight blocks has seven screens,
the sharp support in this template is

\[
                    8n+7\ge 8(d+2)+7=8d+23.             \tag{0.3}
\]

At equality the two owner words are simple, equicardinal, resident, have
the same owner set and the same complete internal interval-OR deck, and
possess nonempty literal maximal `D^d` inverses in one common cap family.
Only one prefix value and one suffix value per phase differ.  They are
screened by two explicit constant-size exterior conditions.

Thus there is a positive **four-central-atom, `O(d)`-support** replacement,
but not a positive literal three-/four-source-star macro.  In fact the two
maximal inverse words differ at `4(d+4)` source positions for `d>=2`.

## 1. The two active paths

Let the active labels be `z,a_0,a_1,a_2,a_3`, with indices modulo four,
and put

\[
 A_i=\{z,a_i\},\qquad B_i=\{a_i,a_{i+1}\}.              \tag{1.1}
\]

The old and new paths are

\[
\begin{aligned}
 W_0={}&B_2,A_2,A_0,B_0,B_1,A_1,A_3,B_3,\\
 W_1={}&B_2,A_3,A_1,B_0,B_1,A_2,A_0,B_3.                \tag{1.2}
\end{aligned}
\]

Both are simple Johnson paths with common endpoints and the same eight
vertices.  At positions `0,2,4,6`, their edges are respectively the four
old and four new octagon atoms.  At positions `1,3,5`, both use the same
three undirected connectors

\[
                         A_0A_2,\quad B_0B_1,\quad A_1A_3. \tag{1.3}
\]

This is precisely the endpoint absorber after its cycle and donor-path
fragments have been contracted.

The active interval-union supports agree.  Their common twenty values are
the four edges/vertices and the active interval unions obtained from
(1.2); direct union gives

\[
                         \mathcal I_\vee(W_0)
                         =\mathcal I_\vee(W_1).          \tag{1.4}
\]

Separate prefix and suffix equality is false.  This is useful rather than
fatal: it localizes all exterior upper damage to one typed value on each
side.

### Proposition 1.1 (the raw four-arm lift is not resident)

Each phase in (1.2) has an internal singleton active-coordinate run.  In
`W_0`, `a_2` occurs alone at `B_1`; in `W_1`, `a_0` occurs alone at `B_0`.
Consequently neither active path is the depth-`d` dilation of a nonempty
source word for any `d>=1`.

#### Proof

A coordinate trace in a `D^d` dilation is a union of intervals of length
`d+1`.  Hence every internal positive run has length at least `d+1`.
The displayed singleton runs violate this necessary condition.  \(\square\)

This is the exact failure of the direct four-arm construction.  Owner and
palette balance alone do not buy residence.

## 2. Coatom tensor

Let `F={f_0,...,f_(n-1)}` be disjoint from the active labels.  For an
active port `V`, define its coatom block

\[
             \mathcal B(V)=
             \bigl(V\cup(F-\{f_0\}),\ldots,
                   V\cup(F-\{f_{n-1}\})\bigr).          \tag{2.1}
\]

Between consecutive active ports `V,W`, put

\[
 I(V,W)=(V\cap W)\cup F,
 \qquad
 U(V,W)=(V\cup W)\cup(F-\{f_0,f_{n-1}\}).              \tag{2.2}
\]

Expand each path in (1.2), using `I` at edge positions `0,2,4,6` and `U`
at positions `1,3,5`.  Call the resulting owner words `X_n,Y_n`.

### Theorem 2.1 (exact local tensor)

For every `n>=2`:

1. `X_n,Y_n` are simple Johnson paths of rank `n+1` and length `8n+7`;
2. their endpoints and owner sets agree;
3. their complete internal interval-union supports agree and have size
   `8n+33`;
4. their clipped endpoint residence signatures agree; and
5. their shortest internal positive run has length exactly `n-1`.

#### Proof

Inside a block, consecutive owners exchange `f_t` and `f_(t+1)`.  At an
intersection screen the last block owner deletes the departing active
label and inserts `f_(n-1)`, while the next step deletes `f_0` and inserts
the arriving active label.  At a union screen these two operations occur
in the opposite order.  Thus every step is Johnson.

The active vertex set is common.  The four intersection screens are the
four lower octagon colours in either phase, and the three union screens
come from the common connectors (1.3).  Hence the owner sets agree.

Intervals wholly inside one block depend only on its active port.  An
interval meeting an intersection screen fills `F` and reduces to an active
interval union.  Near a union screen its filler part is one of

\[
 F-\{f_0,f_{n-1}\},\quad F-\{f_{n-1}\},\quad
 F-\{f_0\},\quad F,                                     \tag{2.3}
\]

and its active part is the union on one of the three common connector
edges.  Formula (1.4) and the common connectors therefore give equality of
the full decks.  The four filler-rank classes are disjoint; direct counting
gives `8n+33`.

For the last assertion, consider a union screen.  It omits `f_0` and
`f_(n-1)`.  Immediately to its left, `f_0` is present in precisely the
last `n-1` owners of the preceding block, bounded by the block's first
owner and the screen, both of which omit it.  This is an internal run of
length `n-1`.  Symmetrically, `f_(n-1)` has a length-`n-1` run immediately
to the right.  Every other internal run is at least this long, by the block
and screen formulas.  \(\square\)

### Corollary 2.2 (sharp residence and support floor)

The tensor is depth-`d` resident if and only if `n>=d+2`.  In particular,
the minimum resident word in this template has length `8d+23`.

#### Proof

Theorem 2.1 gives the necessary and sufficient inequality
`n-1>=d+1`.  Substitution into `8n+7` proves (0.3).  \(\square\)

The support count is also central-sharp within the template.  A one-cycle,
one-donor-path exact exchange has central support at least four by the
quaternary endpoint theorem.  Its four atoms have eight distinct tail/head
ports.  One nonempty coatom block per port therefore requires eight blocks,
and a linear path through them requires seven screens.  A three-central-atom
version would contract to the already-proved support-three obstruction.

## 3. Literal inverse and common cap

Take `n=d+2`.  For phase `epsilon` and source position `p`, define the
maximal inverse letter

\[
 Q_p^\epsilon=
 \bigcap\{(X_n^\epsilon)_i:p-d\le i\le p\},             \tag{3.1}
\]

with the indices clipped to the linear owner word.  The residence statement
together with the explicit block/screen formulas implies, coordinate by
coordinate, both reconstruction and nonemptiness:

\[
                Q_p^\epsilon\ne\varnothing,
 \qquad
                D^d(Q^\epsilon)=X_n^\epsilon.            \tag{3.2}
\]

Put

\[
                         P_p=Q_p^0\cup Q_p^1.             \tag{3.3}
\]

Then `P` is one phase-independent cap family and both literal source words
`Q^0,Q^1` lie below it.  Thus this local tensor passes the common-cap
existence test.  It is not a fixed common source word: for `d>=2`, exactly
`4(d+4)` source positions differ between the two maximal inverses.

The internal upper deck is better than merely bounded: it is identical.
The complete endpoint discrepancy is constant.  With `F` included, the
phase-exclusive prefix values are

\[
\begin{aligned}
 \Pi_0&=F\cup\{z,a_0,a_2,a_3\},\\
 \Pi_1&=F\cup\{z,a_1,a_2,a_3\},                          \tag{3.4}
\end{aligned}
\]

and the phase-exclusive suffix values are

\[
 \Sigma_0=F\cup\{z,a_0,a_1,a_3\},
 \qquad
 \Sigma_1=F\cup\{z,a_0,a_2,a_3\}.                      \tag{3.5}
\]

An exterior prefix union screens (3.4) exactly when it contains both
`a_0,a_1`; an exterior suffix union screens (3.5) exactly when it contains
both `a_1,a_2`.  Hence the crossing upper state has four named typed masks,
independent of `d`.

## 4. Exact scope

The result establishes the smallest currently proved local positive
replacement after the two-star no-go:

\[
\begin{array}{c}
 \text{support-four quaternary endpoint exchange}\\
 +\ \text{resident coatom tensor of block size }d+2\\
 \Downarrow\\
 \text{owner-exact, internally upper-exact, common-cap path pair}\
 \text{on }8d+23\text{ owners, with four endpoint mask obligations.}
\end{array}                                               \tag{4.1}
\]

It does **not** prove that four literal inserted source cells suffice.  The
maximal source phases differ on `4(d+4)` positions.  It also does not plant
the two exterior screening conditions, join the tensor into a global
carrier, or solve the terminal compiler matching.  A construction outside
the one-block-per-port tensor could conceivably beat `8d+23`; (0.3) is not
an architecture-free lower bound.

## 5. Independent audit

Run

```text
python3 scratch/audit_threadD_quaternary_tensor_support_lower_bound_20260801.py
```

The dependency-free replay checks the active paths, the raw singleton-run
obstruction, every `2<=n<=d+2` for `1<=d<=12`, the exact `n-1` witness,
owner/deck equality, endpoint exceptions, maximal inversion, and common
caps.  The frozen output is

```text
scratch/threadD_quaternary_tensor_support_lower_bound_20260801.audit.json
```

and reports

```text
PASS_THREADD_QUATERNARY_TENSOR_SUPPORT_LOWER_BOUND
payload_sha256=a76836f63bf0b9a62094b3d1cc6d6a6abd6d84d1a2e6c55b7a27366241a8b289
```
