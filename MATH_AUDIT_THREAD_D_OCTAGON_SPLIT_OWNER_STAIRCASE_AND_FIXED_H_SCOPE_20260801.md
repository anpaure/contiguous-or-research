# Referee audit: the split octagon has two off-rank boundary staircases

Date: 2026-08-01  
Lane: Thread D, local owner/deadline interface  
Status: exact for `d>=2`, for both maximal and sharp eight-address tensor
inverses.  This note proves local owner rows, source deadlines, residence,
the central q1 path and incidence counts only.  It makes no global host,
upper-factor, Catalan or prescribed-common-cap claim.

## 0. Verdict

Adjoining and splitting

\[
                 X_L=\{a_0,a_1\},\qquad X_R=\{a_1,a_2\}       \tag{0.1}
\]

does not damage any of the `8d+23` central tensor owners.  It creates two
extra owner windows at each side.  Their ranks form the exact staircase

\[
             (r+2,r+1)\mid r^{8d+23}\mid(r+1,r+2).           \tag{0.2}
\]

The whole sequence is a simple path in the Boolean Hasse graph and retains
internal residence floor `d+1`.  Its lower-incidence refinement has

\[
                 16d+48
\]

Hasse edges, of which `16d+44` are the unchanged central Middle-Levels
path and four are off-rank boundary edges.

This distinction controls the fixed-`H` conclusion.  The unconditional
small-protected-factor theorem applies to `H` pairwise vertex-disjoint
central paths when

\[
                         H(16d+44)\le m-2.                   \tag{0.3}
\]

It does **not** plant the `4H` off-rank edges, because those edges do not
belong to the one `ML_m` layer.  Counting all `H(16d+48)` edges would be the
right size for a hypothetical multi-rank Hasse-path extension theorem, but
no such theorem is used here.

## 1. Exact owner windows

Let `Q^epsilon` be either the maximal or sharp exact depth-`d` inverse of
the resident tensor.  Put

\[
        N=|Q^\epsilon|=9d+23,\qquad L=N-d=8d+23.            \tag{1.1}
\]

Let `Phi={f_0,...,f_(d+1)}` and retain the fixed core `K`.  Write the common
endpoint owners as

\[
\begin{aligned}
 C_L&=K\cup(\Phi-\{f_0\})\cup\{a_2,a_3\}=T_0^\epsilon,\\
 C_R&=K\cup(\Phi-\{f_{d+1}\})\cup\{a_0,a_3\}
       =T_{L-1}^\epsilon.                                 \tag{1.2}
\end{aligned}
\]

The two inverse families have the same three-step boundary unions

\[
 \bigcup_{p=0}^{t-1}Q_p^\epsilon=C_L,\qquad
 \bigcup_{p=N-t}^{N-1}Q_p^\epsilon=C_R
 \quad(t\in\{d-1,d,d+1\}).                              \tag{1.3}
\]
Here `d>=2`, so all six displayed intervals are nonempty.  These are the
precise endpoint identities used by the two staircase steps.

In phase `epsilon`, form the split source word

\[
 Y^\epsilon=
 (\{a_\epsilon\},\{a_{1-\epsilon}\},Q_0^\epsilon,\ldots,
 Q_{N-1}^\epsilon,\{a_{2-\epsilon}\},\{a_{1+\epsilon}\}). \tag{1.4}
\]

Let

\[
            O_j^\epsilon=\bigcup_{p=j}^{j+d}Y_p^\epsilon,
            \qquad 0\le j\le L+3.                        \tag{1.5}
\]

### Theorem 1.1 (central survival and exact staircase)

For `0<=i<L`,

\[
                         O_{i+2}^\epsilon=T_i^\epsilon.    \tag{1.6}
\]

The four remaining rows are

\[
\begin{aligned}
 O_0^\epsilon&=C_L\cup\{a_0,a_1\},\\
 O_1^\epsilon&=C_L\cup\{a_{1-\epsilon}\},\\
 O_{L+2}^\epsilon&=C_R\cup\{a_{2-\epsilon}\},\\
 O_{L+3}^\epsilon&=C_R\cup\{a_1,a_2\}.                  \tag{1.7}
\end{aligned}
\]

Consequently

\[
 O_0^\epsilon\supset O_1^\epsilon\supset O_2^\epsilon=C_L,
 \qquad
 C_R=O_{L+1}^\epsilon\subset O_{L+2}^\epsilon
       \subset O_{L+3}^\epsilon,                         \tag{1.8}
\]

and the four off-rank rows have ranks `r+2,r+1,r+1,r+2`.

#### Proof

Every window starting at `i+2` lies wholly in the unchanged `Q` block and
is exactly the old tensor window, proving (1.6).  At start zero both left
halves and `Q_0,...,Q_(d-2)` occur; the `t=d-1` identity in (1.3) gives the
first row of (1.7).  At start one only the packet-near half and
`Q_0,...,Q_(d-1)` occur; the `t=d` identity gives the second row.  At start
two, `Q_0,...,Q_d` gives `C_L`, the `t=d+1` identity.  The three suffix
identities give the last three rows.  Formula (1.2) gives the strict
containments and ranks. \(\square\)

Before splitting, the word `X_L|Q^epsilon|X_R` has only two extra owner
rows, namely the two rank-`r+2` outer rows in (1.7).  Splitting inserts the
two intermediate rank-`r+1` rows.  Relative to the bare tensor, adjoining
the hosts adds two sources and splitting adds two more; relative to an
already-hosted word, the refinement charge is exactly two.

## 2. Source incidence intervals and deadlines

For a source position `p` in a length-`N+4` depth-`d` word, define its
owner-incidence interval and row deadline by

\[
 \mathcal I(p)=
 [\max(0,p-d),\min(p,L+3)],\qquad
 \delta(p)=\min(p,L+3).                                  \tag{2.1}
\]

The four split positions are `0,1,N+2,N+3`.  Their exact data are

\[
\begin{array}{c|c|c}
p&\mathcal I(p)&\delta(p)\\ \hline
0&\{0\}&0\\
1&\{0,1\}&1\\
N+2&\{L+2,L+3\}&L+3\\
N+3&\{L+3\}&L+3.
\end{array}                                               \tag{2.2}
\]

Thus the rank-`r` carrier schedule is exactly the owner-index interval
`[2,L+1]`.  Rows `0,1` are two leading rejected rows and `L+2,L+3` are two
trailing deadline rows.  Formula (2.2) is a chronology statement only: it
does not prove that an ambient compiler permits those four rejections or
the one-position growth of transported intervals.

### Corollary 2.1 (residence survives locally)

The expanded owner word has no strict internal positive run shorter than
`d+1`, and this bound is attained.

#### Proof

The central tensor already has this floor.  At the left boundary, every
coordinate present in a clipped central leading run is either present in
both added rows and remains clipped, or is `f_0`, which is absent already in
`C_L`.  The active endpoint coordinates are `a_2,a_3`, present in both
left rows.  The reversed statement holds at the right boundary with
`f_(d+1)` and `a_0,a_3`.  Hence no clipped short run becomes a strict
internal run. \(\square\)

## 3. q1 path and incidence accounting

Let

\[
                       D_i^\epsilon=T_i^\epsilon\cap T_{i+1}^\epsilon,
                       \qquad0\le i<L-1.                  \tag{3.1}
\]

All `D_i^epsilon` are distinct, and their multiset is phase-independent.
The central lower-incidence lift

\[
 T_0,D_0,T_1,D_1,\ldots,D_{L-2},T_{L-1}                 \tag{3.2}
\]

is therefore a simple path with

\[
                    2(L-1)=16d+44                         \tag{3.3}
\]

incidence edges.  Adjoining the two boundary staircases produces the simple
full-Hasse path

\[
 O_0,O_1,T_0,D_0,\ldots,D_{L-2},T_{L-1},O_{L+2},O_{L+3}, \tag{3.4}
\]

with `16d+48` edges and `16d+49` vertices.

The four new consecutive-owner resource pairs are exactly

\[
\begin{array}{c|cc}
\text{edge}&\text{intersection}&\text{union}\\ \hline
O_0O_1&O_1&O_0\\
O_1T_0&T_0&O_1\\
T_{L-1}O_{L+2}&T_{L-1}&O_{L+2}\\
O_{L+2}O_{L+3}&O_{L+2}&O_{L+3}.
\end{array}                                               \tag{3.5}
\]

They are typed-distinct from the central lower/upper colours in the literal
tensor.  In particular, the central owner and lower-q1 palettes survive
unchanged.  This does not turn the central upper palette into a rainbow: it
still has only 14 distinct upper values.

### Theorem 3.1 (exact fixed-`H` scope)

Suppose `r=m`, the central paths are embedded in the one odd Middle-Levels
host `ML_m`, and `H` selected-phase central paths are pairwise
vertex-disjoint.  The unconditional fixed-`H` protected-factor theorem
applies whenever (0.3) holds.

It applies only to (3.2).  The four off-rank edges per packet lie in the
`r/r+1` and `r+1/r+2` Hasse layers, not in `ML_m`, whose shores have ranks
`m-1,m`.  They remain `4H` explicit endpoint-host obligations.  Hence:

* `H(16d+44)<=m-2` is the proved central q1 planting budget;
* `H(16d+48)` is merely the size of the entire mixed-rank path bank, not an
  antecedent of the existing extension theorem.

For fixed `H` and `d=Theta(sqrt(m))`, the proved central inequality holds
eventually.  No conclusion follows here about global upper coverage,
Catalan connector structure, the external deadline schedule, or one
prescribed common-cap compiler.  The free local cap from the split theorem
is not preserved by an arbitrary factor completion.

## 4. Replay

Run

```text
python3 scratch/audit_threadD_octagon_split_owner_staircase_20260801.py
```

The dependency-free audit checks `2<=d<=12`, both phases, and both maximal
and sharp inverses.  It replays every row in (1.6)--(1.8), the deadlines
(2.2), residence, q1 palette equality, simplicity of (3.2)--(3.4), and both
edge counts.  It intentionally does not call a host solver.
