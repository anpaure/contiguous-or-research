# Rooted pentagonal packets are degree-preserving port pivots, not Catalan-rank absorbers

Date: 2026-08-01  
Lane: protected Catalan connector / pentagonal rotation bank  
Status: exact all-dimensional action, rank lower bound, and literal `m=4`
counterexample to universal post-hoc completion.  A specially selected all-`m`
rooted connector is not refuted.

## 0. Outcome

Relative to a fixed root matching `M0`, an aligned pentagonal `C6` has an
exact and restrictive action.  It keeps the three selected tails, transports
two unused heads across one Johnson square, and preserves the coordinate-load
vector of the residual head bank.  If it maps a rooted Catalan forest to
another forest, both forests still have exactly `Cat_m` components.

Consequently:

1. pentagonal switches inside `Q0` can prepare residual ports, but they add
   **zero** connector rank;
2. `t` packets can improve graphic rank by at most `3t`, so one complete
   rotation orbit can repair at most `6m` rank units;
3. any start with `Cat_m-O(m)` missing connector units needs Catalan-many
   packets or a separately chosen near-spanning selector; and
4. the residual coordinate budgets are invariant under every aligned packet.

The last row gives a literal obstruction.  An upper-exact rooted Catalan
forest on `ML_4` has one available forest-preserving aligned pentagonal pivot,
but its residual left/head coordinate-six loads are `9/8`.  No residual
perfect matching exists before or after that pivot, and no sequence of
aligned pentagonal pivots can repair the deficit.

Thus the orbit bank is not a universal absorber for the exact connector
decomposition.  The surviving positive theorem must choose a good
coordinate-load fibre and high-rank residual matching from the outset.

## 1. Common-root form of the pentagonal packet

Fix a perfect incidence matching `M0` between ranks `m-1,m` of `[2m-1]`.
Retain the five-label notation of
`MATH_THEOREM_CATALAN_PENTAGONAL_C6_PATH_BANK_FORMULA_20260801.md` and name
the physical endpoints

\[
 O=\{AB,CD,EF\},\qquad N=\{AG,DF,EH\}.                 \tag{1.1}
\]

An alignment with the fixed root is

\[
 M_0(L_0)=A,\qquad M_0(L_1)=D,\qquad M_0(L_2)=E.      \tag{1.2}
\]

This is an additional hypothesis, not a consequence of the raw
rotation-bank theorem.  That theorem only says that the switched physical
forest can be oriented after the exchange.  It does not provide one common
`M0` which roots every old and new packet edge while retaining a prescribed
protected shore.  Re-rooting after the switch may move the protected first
matching and the named residual closure, so it is unavailable in the rooted
connector gate unless separately certified.

The corresponding incidence edges in the second shore are

\[
 O_\lambda=\{L_0B,L_1C,L_2F\},\qquad
 N_\lambda=\{L_0G,L_1F,L_2H\}.                       \tag{1.3}
\]

Let `Q` contain `O_lambda`, and suppose `G,H` are unused as heads outside
the packet.  Then replacing `O_lambda` by `N_lambda` is again a matching.
It has the same selected tails and the same three immediate-upper colours,
cyclically reassigned.

### Theorem 1.1 (exact two-head Pluecker pivot)

Let `X` and `Y` be the unused tail and head banks of `Q`.  After (1.3),

\[
 X'=X,\qquad Y'=(Y-\{G,H\})\cup\{B,C\}.              \tag{1.4}
\]

Moreover, writing `chi(V)` for the coordinate-incidence vector of a set,

\[
                 \chi(B)+\chi(C)=\chi(G)+\chi(H),    \tag{1.5}
\]

and therefore

\[
                 \sum_{V\in Y'}\chi(V)
                    =\sum_{V\in Y}\chi(V).          \tag{1.6}
\]

#### Proof

The three tails in (1.3) agree literally.  The old head set is `{B,C,F}`
and the new head set is `{G,F,H}`, which proves (1.4).  Put `P=S+p`.  Then

\[
 \{B,C\}=\{P+q+t,P+r+s\},\qquad
 \{G,H\}=\{P+q+r,P+s+t\}.
\]

Both pairs contain `P` twice and each of `q,r,s,t` once.  This proves
(1.5)--(1.6).  The upper colours are the same three colours by the
pentagonal identity.  \(\square\)

Thus the rooted packet is a square move in one fixed-degree head fibre.  It
is not an arbitrary residual-port exchange.

## 2. Exact graphic action and the Catalan rank budget

Let `K=lambda(Q-O_lambda)` and contract every component of `K`.  The old
and new relative graphic ranks are

\[
 r_K(O_\lambda),\qquad r_K(N_\lambda).                \tag{2.1}
\]

### Theorem 2.1 (relative-rank formula)

For the two equal-cardinality phases,

\[
 c(Q')-c(Q)=r_K(O_\lambda)-r_K(N_\lambda),            \tag{2.2}
\]

where components are counted on the common spanning vertex set.  In
particular the component decrease of one packet is at most three.

If `Q=Q0` is a rooted Catalan forest and `Q'` is also a forest, then

\[
 r_K(O_\lambda)=r_K(N_\lambda)=3,qquad
 c(Q')=c(Q)=\operatorname {Cat}_m.                    \tag{2.3}
\]

For `t` packets, irrespective of interactions,

\[
                  c(Q)-c(Q')\le 3t.                  \tag{2.4}
\]

Hence a single rotation orbit, of size at most `2m`, can pay at most `6m`
component-rank units.

#### Proof

For a spanning graph `H`, `c(H)=|V|-r(H)`.  Additivity after contracting
`K` gives

\[
 r(K\cup O)=r(K)+r_K(O),\qquad
 r(K\cup N)=r(K)+r_K(N),
\]

which proves (2.2).  A three-edge set has relative rank at most three.  If
both results are forests, removing the three old forest edges raises the
component count by three, and the three new edges must lower it by three;
this proves (2.3).  For a bank, delete every old bank edge first and add the
`3t` new edges.  Graphic rank can rise by at most `3t`, proving (2.4).
\(\square\)

This is the exact quantitative mismatch with the connector decomposition.
`Q0` has `Cat_m` components and needs `Cat_m-O(1)` **additional** connector
edges.  Cardinality-preserving switches of `Q0` supply none.  Applied to a
pre-existing cycle cover, one rotation bank can only repair `O(m)` cycles;
it cannot turn an arbitrary Catalan-scale cycle cover into `O(1)` cycles.

## 3. The invariant residual addition budget

For a family `A` of sets, write

\[
 d_i(A)=|\{Z\in A:i\in Z\}|.                          \tag{3.1}
\]

### Theorem 3.1 (coordinate budget and protected closure)

If the residual incidence graph between `X` and `Y` has a perfect matching,
then

\[
                         d_i(Y)-d_i(X)\ge0             \tag{3.2}
\]

for every coordinate `i`.  If a protected residual matching `R_*` is
prescribed and `h_i` of its edges add coordinate `i`, then necessarily

\[
                         d_i(Y)-d_i(X)\ge h_i.         \tag{3.3}
\]

For a rooted Catalan forest `Q0`, one also has

\[
 d_i(Y)-d_i(X)=\operatorname {Cat}_{m-1}-a_i,         \tag{3.4}
\]

where `a_i` is the number of `Q0` edges which add coordinate `i`.  Every
aligned pentagonal pivot preserves `X`, every `d_i(Y)`, and hence every
`a_i` and every inequality (3.2)--(3.3).

#### Proof

In an incidence matching, the matched head is the tail plus one coordinate.
Thus `d_i(Y)-d_i(X)` counts residual matching edges which add `i`, proving
(3.2); reserving `R_*` proves (3.3).  Across the two complete shores,

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}
                 ={1\over m}{2m-2\choose m-1}
                 =\operatorname {Cat}_{m-1}.         \tag{3.5}
\]

Subtracting the used `Q0` tails and heads gives (3.4).  Theorem 1.1 proves
invariance.  \(\square\)

For one protected residual closure which adds coordinate `i`, the weakest
packet-compatible rooted state must therefore export the literal margin
`d_i(Y)-d_i(X)>=1`, not merely ordinary unrooted palette equality.

## 4. Literal `m=4` obstruction with one live pivot

The replay freezes a perfect `M0` on ranks `3/4` of `[7]` and a matching
`Q0` of size `21`.  It verifies:

\[
 \operatorname{up}(Q_0)={[7]\choose5},\qquad
 r_{\rm gr}(\lambda(Q_0))=21,
\]

so `Q0` is an upper-exact rooted Catalan forest with

\[
                         35-21=14=\operatorname {Cat}_4
\]

components.  Its residual banks have size `14`, but

\[
 (d_i(Y)-d_i(X))_{i=0}^6=(4,2,2,3,3,1,-1).           \tag{4.1}

In particular, nine left holes contain coordinate six and only eight head
holes do.  No residual perfect matching is possible.  Direct matching gives
rank `11/14`.

There is exactly one available aligned pentagonal packet which keeps the
result a rooted Catalan forest:

\[
 \begin{aligned}
 O_\lambda&=\{(0x0b,0x0f),(0x15,0x35),(0x29,0x2b)\},\\
 N_\lambda&=\{(0x0b,0x2b),(0x15,0x17),(0x29,0x2d)\}.
 \end{aligned}                                       \tag{4.2}
\]

It replaces head holes `{0x17,0x2d}` by `{0x0f,0x35}`.  All four avoid
coordinate six, so (4.1) is unchanged; direct residual matching remains
`11/14`.  By Theorem 1.1, every subsequent aligned pentagonal sequence is
trapped in the same impossible degree fibre.

This is a counterexample to

\[
 \boxed{\text{rooted Catalan forest + available pentagonal pivots}
        \Longrightarrow\text{residual connector completion}.}       \tag{4.3}
\]

It does not refute selecting a different `Q0` whose residual degree vector,
matching row and graphic rank are jointly feasible.

## 5. Exact surviving selector and split-letter interface

The proof-safe all-`m` target is therefore not a post-hoc packet absorber.
It must select, simultaneously,

1. a protected rooted Catalan forest `Q0` in a degree-admissible fibre;
2. a residual perfect matching containing the protected closure and having
   contracted graphic rank `Cat_m-O(1)`; and
3. only then, any clean pentagonal packets used to navigate within that
   fibre without losing the protected head.

In addition, a rotation-closed bank used at this stage needs a **common-root
certificate**: all of its local alignments (1.2) must extend one fixed `M0`
containing the protected first shore.  Physical forest orientability alone
does not imply this row.

The split-letter theorem can pay `O(1)` named **mask** debts once actual
dominating source letters are present.  Block contraction is incidence- and
component-neutral: it neither changes (3.4) nor creates one of the
`Cat_m-O(1)` connector edges.  Therefore it can finish bounded upper/compiler
casualties after this selector, but cannot replace it.

## 6. Mechanical replay

Run

```text
python3 scratch/audit_catalan_pentagonal_rooted_port_pivot_20260801.py
```

The script checks the dimension-free load identity for `3<=m<=12`, the
literal `M0,Q0` certificate, upper exactness, forest rank, the unique live
rooted packet, both residual matching ranks, and the invariant Hall deficit.
Expected status:

```text
PASS_CATALAN_PENTAGONAL_ROOTED_PORT_PIVOT_OBSTRUCTION
```
