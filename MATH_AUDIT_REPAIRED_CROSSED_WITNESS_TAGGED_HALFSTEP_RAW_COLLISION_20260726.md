# Audit of the repaired crossed witness, tagged half-steps, and raw-target collisions

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Three distinct statements must be separated.

1. The originally proposed crossed witness is false.  It applies the
   old witness factor at the opposite half-state and therefore does not
   preserve the same-owner direction relation.
2. A repaired crossed witness exists.  It is a neighbour permutation by
   an explicit inverse and gives the required direction relation at every
   composite owner.  Its cycle structure is irrelevant: the affine
   complete-mapping lemma needs only the zeroth row factor to have the
   required physical cycles.
3. The four half-step sectors reduce exactly to aligned codes after the
   moved support and boundary roles are supplied as tags.  This does not
   imply literal OR injectivity.  There are explicit lower and upper
   depth-one collisions with different moved supports already in the
   `r=4` seed.

Thus the repaired recursion restores the tagged-code theorem, but the
literal local gate is

\[
 \text{recover the support and boundary roles from the raw target,}
\tag{0.1}
\]

or else prove disjointness between the raw images belonging to different
tags.

## 1. The old crossed child is false

Let `G_0,G_1` be the corrected `Q_4` pair, with

\[
                         \delta_1(z)=S\delta_0(z),
 \qquad                  S=(2\ 4).
\tag{1.1}
\]

For `epsilon(u,v)=|u|+|v| mod 2`, the row child is

\[
 P_0(u,v)=
 \begin{cases}
  (G_0u,v),&\epsilon=0,\\
  (u,G_0v),&\epsilon=1.
 \end{cases}
\tag{1.2}
\]

The false witness was

\[
 \widetilde P_1^\times(u,v)=
 \begin{cases}
  (u,G_1v),&\epsilon=0,\\
  (G_1u,v),&\epsilon=1.
 \end{cases}
\tag{1.3}
\]

Take `u=0000`, `v=1100`.  They have the same parity, while

\[
                         \delta_0(u)=1,
 \qquad                  \delta_1(v)=3.
\tag{1.4}
\]

Thus `P_0` uses `L1`, whose required crossed image is `R1`, but
`widetilde P_1^times` uses `R3`.  The base relation (1.1) compares the two
directions at the same vertex; equal parity of `u,v` is insufficient.

## 2. The repaired crossed witness

Let `G_0` be any neighbour permutation of `Q_h`, with outgoing direction
`delta_0`, and let `S` be any coordinate permutation.  Define

\[
 C_S(u,v)=
 \begin{cases}
  (u,v\oplus e_{S\delta_0(u)}),&\epsilon(u,v)=0,\\
  (u\oplus e_{S\delta_0(v)},v),&\epsilon(u,v)=1.
 \end{cases}
\tag{2.1}
\]

Define the crossed coordinate permutation by

\[
                         S^\times(Li)=R(Si),
 \qquad                  S^\times(Ri)=L(Si).
\tag{2.2}
\]

### Theorem 2.1

The map `C_S` is a neighbour permutation and

\[
                         \delta_{C_S}(u,v)
                         =S^\times\delta_{P_0}(u,v)
\tag{2.3}
\]

at every owner.

#### Proof

An odd target `(u,v)` has the unique even predecessor

\[
                         (u,v\oplus e_{S\delta_0(u)}),
\tag{2.4}
\]

while an even target has the unique odd predecessor

\[
                         (u\oplus e_{S\delta_0(v)},v).
\tag{2.5}
\]

Hence `C_S` is bijective and every move is a cube edge.  At an even
owner, `P_0` uses `Li`, where `i=delta_0(u)`, and `C_S` uses `R(Si)`.
At an odd owner the two directions are `Ri`, with `i=delta_0(v)`, and
`L(Si)`.  This is (2.3).  \(\square\)

If every component of `G_0` is an isometric `C_(2h)`, every component of
`P_0` is an isometric `C_(4h)`: `P_0^2(u,v)=(G_0u,G_0v)`, and the first
half of each child direction word uses every coordinate once.  The cycle
structure of `C_S` is not used by the affine lemma.  Therefore

\[
                         (P_0,C_S,S^\times)
\tag{2.6}
\]

is a valid recursive complete-mapping certificate.

## 3. Exact four-sector half-step enumeration

For an even coarse context `p`, write the lifted forward orbit as

\[
 E_t=(p,x_t)
 \xrightarrow{b_{i_t}}
 O_t=(p\oplus e_{i_t},x_t)
 \xrightarrow{a_{i_t}}
 E_{t+1}=(p,x_t\oplus e_{i_t}).
\tag{3.1}
\]

Put `i_s=i_(t+s)`.  If the moved support and partial-boundary roles are
included in the code, the four sectors are

\[
\begin{array}{c|c|l|c}
\text{start}&\text{length}&\text{direction word}
 &\text{aligned code determined}\\ \hline
E_t&2d&(b_{i_0}a_{i_0})\cdots(b_{i_{d-1}}a_{i_{d-1}})
 &\mathcal C_d^+(p,x_t)\\
E_t&2d+1&(b_{i_0}a_{i_0})\cdots(b_{i_{d-1}}a_{i_{d-1}})b_{i_d}
 &\mathcal C_{d+1}^+(p,x_t)\\
O_t&2d&a_{i_0}(b_{i_1}a_{i_1})\cdots
 (b_{i_{d-1}}a_{i_{d-1}})b_{i_d}
 &\mathcal C_{d+1}^+(p,x_t)\\
O_t&2d+1&a_{i_0}(b_{i_1}a_{i_1})\cdots(b_{i_d}a_{i_d})
 &\mathcal C_{d+1}^+(p,x_t).
\end{array}
\tag{3.2}
\]

The third row assumes `d>=1`; the fourth includes `d=0`.  In the first
row the completed envelope is `{i_0,...,i_(d-1)}`.  In every other row it
is `{i_0,...,i_d}`.

For every coordinate `k` outside this envelope, neither physical bit is
moved, and the target records

\[
                         x_k=a_k,
 \qquad                  p_k=a_k\oplus b_k.
\tag{3.3}
\]

Thus no exterior `p`- or `x`-bit is lost.  The partial boundary endpoints
are extra data; the aligned code in the final column needs only the union
of the completed and partial directions.

For reverse traversal one coarse pair has word `a_j,b_j`.  Interchanging
`a,b` in (3.2) and replacing the forward direction sequence by the
backward sequence gives the four reverse sectors and the corresponding
aligned reverse codes.  Hence tagged aligned injectivity through depth
`H` implies tagged half-step injectivity whenever the completed envelope
has size at most `H`.

## 4. The tag is not contained in a raw target

On one pair, a completed move can be

\[
                         00\longrightarrow01\longrightarrow11.
\tag{4.1}
\]

Its lower restriction is indistinguishable from an untouched `00` pair,
and its upper restriction from an untouched `11` pair.  A partial move
can likewise have the same restriction as an untouched split pair.

There are actual whole-cell collisions.  In the `r=4` seed take
`p=0000`.  The direction values

\[
 \delta_0(1010)=1,\qquad \delta_0(0010)=2
\tag{4.2}
\]

give lower targets

\[
\begin{array}{c|c|c}
x&J&\text{pair-state target}\\ \hline
1010&\{1\}&(00,00,11,00)\\
0010&\{2\}&(00,00,11,00).
\end{array}
\tag{4.3}
\]

Likewise

\[
 \delta_0(0101)=1,\qquad \delta_0(1101)=2
\tag{4.4}
\]

give the same upper target

\[
                         (11,11,00,11)
\tag{4.5}
\]

with supports `{1}` and `{2}`.  Thus even depth-one tagged injectivity
does not imply raw lower or upper injectivity.

## 5. Exact boundary

Proved:

* the old crossed recursion is false;
* the repaired witness (2.1) is an exact neighbour permutation satisfying
  the same-owner relation;
* all four forward and reverse half-step sectors reduce to aligned codes
  without losing an exterior bit, when their support roles are tagged;
* the tag is not a deterministic function of a raw target; and
* literal lower and upper cross-tag collisions occur in the finite seed.

Not proved:

* recovery of support and boundary roles from raw targets in the growing
  recursion;
* disjointness of different tagged images there; or
* the outer packet coupling.

