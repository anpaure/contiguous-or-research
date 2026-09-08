# A valid crossed column witness for the late-cross affine compiler

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The formerly claimed crossed product of two double factors is false, but
the same fixed-point-free context permutation has a different, valid
column witness.

Let `G` be any neighbour permutation of `Q_h`, with outgoing direction
field `delta`, and let `S` be any permutation of its `h` coordinate
labels.  Define the parity-alternating zeroth factor

\[
 R(G)(u,v)=
 \begin{cases}
  (Gu,v),&|u|+|v|=0,\\
  (u,Gv),&|u|+|v|=1,
 \end{cases}                                         \tag{0.1}
\]

and define a crossed shorewise translation

\[
 C_S(G)(u,v)=
 \begin{cases}
  (u,v+e_{S\delta(u)}),&|u|+|v|=0,\\
  (u+e_{S\delta(v)},v),&|u|+|v|=1.
 \end{cases}                                         \tag{0.2}
\]

Let

\[
 S^\times(Li)=R(Si),\qquad
 S^\times(Ri)=L(Si).                                \tag{0.3}
\]

Then `C_S(G)` is a neighbour permutation and, owner by owner,

\[
       \boxed{\delta_{C_S(G)}(u,v)
                    =S^\times\delta_{R(G)}(u,v).}    \tag{0.4}
\]

Thus `(R(G),C_S(G),S^times)` is a valid affine complete-mapping
certificate.  No cycle or incoming-direction hypothesis on `C_S(G)` is
needed.  If `G` factors `Q_h` into isometric `C_(2h)`'s, then `R(G)`
factors `Q_(2h)` into isometric `C_(4h)`'s, and the final affine parity
lift is an exact physical isometric factor.

Applying (0.1)--(0.4) once to the `Q_4` zeroth factor and then using the
valid parallel recursion restores the late-cross **augmented** trace-code
construction.  Its blockwise puncturing decoder remains correct whenever
the support `J` is supplied.  It does not repair the independent fact that
a literal lower or upper target need not determine `J`.

## 1. The shorewise translation is a permutation

Put

\[
 E=\{(u,v):|u|+|v|=0\},\qquad
 O=\{(u,v):|u|+|v|=1\}.                             \tag{1.1}
\]

Every clause of (0.2) toggles one coordinate, so `C_S(G)` sends `E` to
`O` and `O` to `E`.

### Lemma 1.1 (explicit shorewise inverses)

The restrictions of `C_S(G)` to the two parity shores are bijections.
Their inverses are

\[
 \begin{aligned}
 C_S(G)|_E^{-1}(u,w)
   &=(u,w+e_{S\delta(u)}) && ((u,w)\in O),\\
 C_S(G)|_O^{-1}(w,v)
   &=(w+e_{S\delta(v)},v) && ((w,v)\in E).
 \end{aligned}                                       \tag{1.2}
\]

#### Proof

On `E`, the first half `u` is fixed and the second half is translated by
the unit vector `e_(S delta(u))`.  The displayed first formula reverses
that translation.  On `O`, the second half `v` is fixed and the first
half is translated by `e_(S delta(v))`; the second formula reverses it.
The two restrictions have disjoint target shores, so together they make
one permutation of `Q_(2h)`.  \(\square\)

Notice that `C_S(G)` need not be an involution: after one move its other
clause may evaluate `delta` at a different state.  The shorewise inverse,
not an involution claim, proves permutation.

## 2. Exact same-owner crossed relation

### Theorem 2.1 (crossed column witness)

Equations (0.1)--(0.3) satisfy (0.4) at every owner.

#### Proof

At an even owner `(u,v)`, the zeroth direction is

\[
                         L\delta(u),                 \tag{2.1}
\]

while the witness direction is

\[
                         R(S\delta(u))
             =S^\times(L\delta(u)).                 \tag{2.2}
\]

Both fields are evaluated at the same child state `u`.  At an odd owner,
the corresponding directions are

\[
                         R\delta(v),
 \qquad                  L(S\delta(v))
             =S^\times(R\delta(v)).                 \tag{2.3}
\]

and both are evaluated at `v`.  This proves (0.4).  \(\square\)

This is precisely what failed in the old definition: its even witness
used `delta_1(v)` while its zeroth field used `delta_0(u)`.

## 3. Affine complete mapping needs no extra witness geometry

Let

\[
                         G_0=R(G),
 \qquad                  G_1=C_S(G),
 \qquad                  \Sigma=S^\times.           \tag{3.1}
\]

For an even context `p in Q_(2h)` and `x in Q_(2h)`, put

\[
 y=\Sigma p+x,qquad
 d_p(x)=\delta_{G_0}(y),qquad
 F_p(x)=x+e_{d_p(x)}.                               \tag{3.2}
\]

### Theorem 3.1 (exact column bijection)

Every `F_p` is a translated conjugate of `G_0`, and for every `x` the map

\[
                         T_x(p)=p+e_{d_p(x)}         \tag{3.3}
\]

is a bijection from the even context shore to the odd shore.

#### Proof

Translation by `Sigma p` gives

\[
 \Sigma p+F_p(x)=G_0(\Sigma p+x)=G_0(y).            \tag{3.4}
\]

Thus the rows are conjugates of `G_0`.  By (0.4),

\[
 \Sigma T_x(p)+x
  =y+e_{\Sigma\delta_{G_0}(y)}
  =y+e_{\delta_{G_1}(y)}
  =G_1(y).                                          \tag{3.5}
\]

The affine map `p -> Sigma p+x` bijects each parity shore with one parity
shore, and the neighbour permutation `G_1` bijects opposite shores.
Equation (3.5) proves the column bijection.  \(\square\)

Only two facts about `G_1` occur in this proof:

1. it is a neighbour permutation; and
2. its outgoing direction obeys (0.4).

No incoming relation, cycle length, or isometry of `G_1` is used.

## 4. Cycle and reverse-trace dependence

Suppose every component of `G` is an isometric `C_(2h)`.  The usual
alternation calculation gives

\[
                         R(G)^{2s}(u,v)=(G^su,G^sv). \tag{4.1}
\]

During the first `2h` moves, each child makes `h` consecutive parent
moves and uses every parent direction once.  The next `2h` directions
repeat.  Hence `R(G)` consists of isometric `C_(4h)`'s.

By (3.4), every affine row `F_p` is a translated copy of `R(G)`.  In the
physical parity lift, two physical moves simulate one `F_p` move, so its
cycle structure and isometry depend only on `G_0=R(G)`, not on `G_1`.
Likewise, the even-time reverse trajectory is conjugate to `G_0^{-1}`.
Thus reverse augmented-trace decoding needs the incoming fibres of the
zeroth factor only; it needs no incoming identity for the column witness.

## 5. Iteration and exact scope

Starting from the audited `Q_4` zeroth factor with `S_4=(2 4)`, equations
(0.1)--(0.4) give a valid dimension-eight certificate with fixed-point-
free context involution

\[
 S_8(Li)=R(S_4i),\qquad S_8(Ri)=L(S_4i).             \tag{5.1}
\]

At higher dimensions use the parallel recursion on this valid
certificate.  If `(H_0,H_1,T)` is a certificate, define

\[
 P_j(u,v)=
 \begin{cases}
  (H_ju,v),&|u|+|v|=0,\\
  (u,H_jv),&|u|+|v|=1.
 \end{cases}                                         \tag{5.2}
\]

The map `P_j` is a neighbour permutation because

\[
                         P_j^2(u,v)=(H_ju,H_jv),     \tag{5.3}
\]

and a map whose square is bijective is bijective.  At the same selected
child owner, the direction fields obey the direct-sum relation

\[
              \delta_{P_1}=(T\oplus T)\delta_{P_0}. \tag{5.4}
\]

Thus the context involution at dimension `R=8*2^t` is the blockwise
direct sum of `2^t` copies of `S_8`, exactly as required by the late-cross
augmented-code decoder.

The repaired conclusion is therefore:

* exact row factors and exact column bijections are restored;
* the zeroth factor, its direction supports, and all forward/reverse
  puncturing calculations are unchanged;
* the augmented code with externally supplied `J` is exactly injective in
  the previously proved one-visit range;
* literal physical lower/upper injectivity does not follow, because the
  target may not determine `J`.

The last point is an independent carrier-identification gate, not a defect
of the repaired column witness.
