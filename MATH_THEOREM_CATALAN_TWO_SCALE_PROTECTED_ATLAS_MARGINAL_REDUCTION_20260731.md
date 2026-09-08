# Two-scale protected absorption: exact marginal reduction and the Catalan long-ear gate

Date: 2026-07-31  
Status: exact conditional reduction, exact constants, and a sharp abstract
barrier for one-point common-basis marginals.  No dimension-uniform local
actuator embedding or fixed-`Q` long-ear packing theorem is claimed.

## 0. Verdict

There is a rigorous two-scale implication, but its quantifiers and guards
must be stated literally.

Suppose that, **before** the synchronized common basis `Q` is selected, a
bank of defect tokens has been given private local packet menus.  An option
for token `i` has a declared risk set `R` in the actual common-basis ground
set; avoiding `R` is sufficient for the option to survive in the fixed-`Q`
side host.  If the average declared risk of token `i` is `ell_i`, the
balanced common-basis distribution selects a common basis for which at most

```text
                         (C/N) sum_i ell_i                 (0.1)
```

tokens have no certified surviving option.  This is a first-moment identity;
it uses no independence or negative dependence.  If there are `O(P)` tokens
and every risk is bounded, (0.1) is `O(P/n)=O(Cat_(n+1))`.

The conclusion is useful only if the packet bank is a genuinely guarded
private cube: every simultaneous subset choice must preserve the two outer
palettes, capacity slots, protected seams and anchors, contracted physical
acyclicity, the required root row, and an explicitly exported downstream
compiler cap.  Those properties are hypotheses on the atlas, not
consequences of one-point marginals.

The Catalan residual scale is sharp for the marginal argument.  In the
singleton-risk system on the whole common-basis ground set every common
basis kills exactly `C` tokens.  Even after restricting to any `P` singleton
risks, cardinality alone permits a forced loss of

```text
                    C-(N-P)=N/n=Cat_n.                  (0.2)
```

Thus a zero-defect proof needs a second, fixed-`Q` theorem.  Its exact form
is a protected positive-gain outside matching in the exchange host, with a
contracted graphic/root certificate and a literal compiler-cap certificate.
The residual has Catalan order, so `Theta(n)` ears have scalar total support
`Theta(P)`, but their coefficients, installation, and correlation are
load-bearing.  The existing private-circuit capacity audit gives necessary
budgets only; it does not construct this long-ear bank.

## 1. Exact scales

For `n>=4`, put

```text
K = Cat_n,
N = binom(2n,n-1),
P = binom(2n,n-2),
C = Cat_(n+1),
q = C/N.                                                (1.1)
```

The elementary identities needed below are

```text
N = nK,
P = n(n-1)K/(n+2),
C = 2(2n+1)K/(n+2),
q = 2(2n+1)/(n(n+2)),                                  (1.2)

N/P = (n+2)/(n-1),
qP = C(n-1)/(n+2) < C,
nC = (4+6/(n-1))P,                                     (1.3)

N-P = 3P/(n-1),
C-(N-P) = N/n = K.                                     (1.4)
```

In particular

```text
P/n = [(n-1)/(2(2n+1))] C.                             (1.5)
```

Thus `C`, `K`, and `P/n` are the same asymptotic scale, with exact
coefficients available from (1.2)--(1.5).

The automatic-common-basis theorem supplies a probability distribution
`mu` on synchronized common bases `Q subseteq E`, where `|E|=N` and
`|Q|=C`, satisfying

```text
                         Pr_mu(e in Q)=q                 (1.6)
```

for every `e in E`.  Nothing below assumes more than (1.6).

## 2. Risk menus and the exact averaging theorem

Let `I` be a finite token set.  Token `i` has a nonempty finite option menu
`A_i`.  For every option `a in A_i`, specify a risk set

```text
                         R_(i,a) subseteq E.             (2.1)
```

The intended meaning is one-way and literal:

> if `Q cap R_(i,a)` is empty, then option `a` has a certified realization
> in the fixed-`Q` host.

The option may also survive when the declared risk is met; (2.1) is only a
sufficient certificate.  Risks in a palette, slot, owner, physical-edge, or
compiler-cell ground set cannot be inserted into (2.1) unless an explicit
map to the common-basis ground `E` has been proved.

Choose arbitrary probability weights `lambda_(i,a)` on each menu and put

```text
ell_i = sum_(a in A_i) lambda_(i,a) |R_(i,a)|.          (2.2)
```

Call token `i` **uncertified** for `Q` if every one of its options has its
declared risk met.

### Theorem 2.1 (exact weighted marginal reduction)

There is a synchronized common basis `Q` for which the uncertified token
set `U(Q)` satisfies

```text
                  |U(Q)| <= floor(q sum_i ell_i).       (2.3)
```

More generally, for arbitrary nonnegative token weights `w_i`, some `Q`
satisfies

```text
       sum_(i in U(Q)) w_i
          <= q sum_i w_i ell_i.                         (2.4)
```

Consequently:

* if `|I|<=cN` and `ell_i<=L`, then `|U(Q)|<=cLC`;
* if `|I|<=cP` and `ell_i<=L`, then

  ```text
  |U(Q)| <= cL C(n-1)/(n+2) < cLC;                     (2.5)
  ```

* in particular, `O(P)` constant-risk tokens leave only `O(P/n)`
  uncertified tokens.

#### Proof

If `i` is uncertified, then every option risk meets `Q`; hence

```text
1_(i in U(Q))
 <= sum_(a in A_i) lambda_(i,a) |Q cap R_(i,a)|.        (2.6)
```

Multiply by `w_i`, sum over `i`, and average over `mu`.  By (1.6),

```text
E_mu |Q cap R_(i,a)| = q |R_(i,a)|.                    (2.7)
```

Equations (2.6)--(2.7) give the right side of (2.4).  Some common basis has
cost no greater than its average.  With unit weights the left side is an
integer, giving the floor in (2.3).  Substituting `qN=C` proves the first
bullet, and substituting (1.3) proves (2.5).  `square`

### Corollary 2.2 (guarded private-cube reduction)

Suppose in addition that the menus form the following uniform guarded
atlas.

1. For every selected common basis `Q`, the fixed-`Q` construction exposes
   a partial state whose actual defect bank `J_Q` is a subset of `I`.
   In the unit cover-down application these are literal gain-one defects:
   the current matching has deficiency `|J_Q|`, and activating token `i`
   removes exactly one unit of that deficiency without creating another.
2. For every `i in J_Q-U(Q)`, one certified option can be selected, and any
   such simultaneous cross-token selection is incidence-private in the
   outer palettes and capacity slots.
3. Every subset of those packet activations lies on the same protected
   graphic/root face after contraction of the fixed scaffold.
4. Every subset state retains one displayed compiler SDR, or passes an
   explicitly proved self-breaking blocker/deadline system for the final
   common cap.

Then a common basis and a simultaneous local activation exist whose
remaining defect set is contained in `U(Q)` and hence obeys (2.3)--(2.5).
In the unit cover-down application its matching deficiency obeys the same
bound.  All named seams, anchors, roots, and compiler cells in the guarded
cube are preserved.  For nonunit defects the identical statement uses
Theorem 2.1 with `w_i` equal to the required gain of token `i`.

#### Proof

Choose `Q` by Theorem 2.1.  Activate one certified option for every token in
`J_Q-U(Q)`.  Conditions 2--4 say exactly that their union is a legal state
and creates no new guarded defect.  Therefore only `J_Q cap U(Q)` can
remain, and this is a subset of `U(Q)`.  `square`

Corollary 2.2 is intentionally conditional.  The arbitrary-`Q`
Delcourt--Postle theorem supplies a large bulk for each `Q`, but it does not
say that the bulk leave is `J_Q`, that the off states of the atlas are
installed in that bulk, or that all certified menus are jointly private.

## 3. What “private” must include

Resource-disjoint packet drawings are not by themselves enough for
Corollary 2.2.

### 3.1 Palette and slot rows

Each packet state must be a matching in the fixed four-resource slot host.
Cross-token privacy must include both outer-colour shores and every physical
owner slot.  A risk certificate in `E` does not certify either assertion.

### 3.2 Physical graphic and root rows

Delete all packet off states and contract the retained fixed physical
forest.  The links offered by the selected packet states must be independent
in the resulting graphic matroid.  If every final component must contain
one designated root, the selected link forest must also satisfy the literal
component-root equation.  Graphic independence gives the “at most one”
part after root edges are encoded; it does not automatically give the
“at least one” part.

### 3.3 Common-cap row

Once a side matching is outer-perfect and its physical support is a forest,
the local Boolean two-step common cap is automatic.  The later
maximal-envelope/word compiler cap is not.  A packet atlas must therefore
export either

* one literal target-to-cell SDR surviving every subset state; or
* the exact blocker self-breaking and serialization inequalities for every
  reachable compiler blocker.

Marginal survival of packet incidences cannot replace this integral row.

### 3.4 Quantifier order

The atlas and its risk map must be specified before choosing `Q`; its
certified realization may depend on `Q`.  If the packets are first found in
one already fixed host and their risk sets are then assigned retroactively,
Theorem 2.1 says nothing.  Conversely, the Delcourt--Postle bulk may be
chosen after `Q` only if its leave is guaranteed to lie in the atlas token
bank and the required packet off states are installed.

## 4. Sharp obstruction for one-point marginals

Theorem 2.1 has the correct order and, as a statement using only
one-point marginals, cannot be upgraded to zero defect.

### Proposition 4.1 (singleton-risk equality)

Take one token `i_e` for every `e in E`, with one option and risk
`R_(i_e)={e}`.  Every common basis has exactly

```text
                         |U(Q)|=|Q|=C.                  (4.1)
```

Thus (2.3) is equality because `q sum_i ell_i=qN=C`.

If instead singleton-risk tokens are put on any fixed set `A subseteq E`
of order `P`, then every `C`-element common basis obeys

```text
|U(Q)|=|Q cap A|
 >= C-(N-P)
 = K.                                                  (4.2)
```

#### Proof

Equation (4.1) is immediate.  For (4.2), at most `N-P` elements of `Q` can
lie outside `A`; now use (1.4).  `square`

This is an abstract risk-interface obstruction, not a claim that the
Boolean fixed-four host realizes a private singleton-risk atlas.  It proves
the logical point needed here: exact uniform marginals alone naturally stop
at Catalan scale.  Multiple alternatives do not change this conclusion
without a joint-avoidance theorem; (1.6) contains no negative-dependence or
concentration assertion.

## 5. The exact fixed-`Q` long-ear finish

After the unit-gain local activation of Corollary 2.2, fix the selected
common basis `Q`.  Let `M` be the resulting host matching, let
`h=P-|M|`, let `Z subseteq M` be protected old atoms, and let `F_fix` be the
frozen physical scaffold and seams.  For a host matching
`S subseteq E(G_Q)-M`, put

```text
N_M(S)={m in M : m shares a host resource with some s in S}.       (5.1)
```

The exact matching/physical finish required at the second scale is:

```text
|S|-|N_M(S)| = h,                                      (5.2)
N_M(S) cap Z = empty,                                  (5.3)
phi(S) is graphic-independent after contracting
       F_fix union phi(M-N_M(S)).                       (5.4)
```

Here `phi` is physical projection.  Equations (5.2)--(5.4) are precisely
the protected gain and positive-cut criterion from the full-colour
cover-down theorem.  They are necessary and sufficient for replacing
`N_M(S)` by `S` to produce a size-`P` host matching whose union with the
fixed scaffold is a forest and which retains every protected old atom.

For the recursive application the following rows must be appended
literally:

1. every final physical component has the prescribed root/anchor type;
2. the final state has the required protected seam incidences;
3. the final matching has the exported compiler SDR/common cap; and
4. if intermediate states matter, the inclusion-minimal positive exchange
   components admit the proved SCC/blocker-deadline serialization.

Call the assertion that such an `S` exists for every residual output of
Corollary 2.2 with

```text
                         h <= q sum_i ell_i              (5.5)
```

the **Catalan-scale installed long-ear theorem**.  This is the exact second
stage needed for zero defect.  It is a fixed-`Q` theorem: the long ears must
live in the punctured host and their common off states must occur in `M`.

### 5.1 Scalar scale versus actual capacity

If (5.5) is at most `lambda C` and every selected long ear has `O(n)`
support, then its total support has order at most

```text
                         O(nC)=O(P),                    (5.6)
```

using (1.3).  Equation (5.6) is only an order calculation.

For an exact necessary coefficient audit, suppose the old parts of the
long ears are pairwise private and each contains at least `an` old matching
atoms.  Across two side matchings there is room for at most

```text
                         2P/(an)                        (5.7)
```

tokens, and on one shore at most `P/(an)`.  If stage one has `|I|<=cN` and
`ell_i<=L`, its worst guaranteed residual `cLC` can fit the two-shore scalar
budget only if

```text
                         acL <= (n-1)/(2n+1),           (5.8)
```

and a one-shore concentration requires

```text
                         acL <= (n-1)/(2(2n+1)).        (5.9)
```

These are necessary capacity rows, not existence theorems.  They agree with
the independent stage-two private-circuit audit.  In particular, big-Oh
compatibility does not justify discarding the constants.

### 5.2 Why the long bank cannot simply be pre-reserved

A length-`Theta(n)` ear fixed before `Q` has `Theta(n)` common-basis risk,
so `q ell=Theta(1)` and Theorem 2.1 does not give `1-o(1)` survival.  A
Catalan number of pairwise-private installed old parts of length
`Theta(n)` occupies `Theta(P)` old matching atoms.  Protecting their entire
closed support and then applying the existing Delcourt--Postle reserve
theorem loses `Theta(P)`, not `o(P)`.

Therefore the second stage must be chosen after or jointly with `Q` and
installed jointly with the bulk matching.  A conditional/reservoir colour
theorem, a many-token amortized circuit, or a structured shorter-distance
pairing could supply it; none is currently proved.

## 6. Exact scope

This note proves:

* the exact weighted common-basis risk reduction (2.3)--(2.5);
* its composition with a genuinely private, subset-guarded packet cube;
* the sharp Catalan-order singleton-risk barrier (4.1)--(4.2); and
* the exact protected gain/graphic/root/compiler interface required of the
  fixed-`Q` long-ear finish.

It does **not** prove:

* that the transparent `ML(7)` incidence hexagon, the fixed `n=3` side
  actuator, or an AGCF `2 -> 3` packet embeds in the fixed-four side-slot
  host;
* a constant-risk guarded atlas in that host;
* an aligned Delcourt--Postle bulk leave or installed packet off states;
* the Catalan-scale long-ear theorem; or
* residence, deeper shadows, the word compiler, or `nu(k)=B(k)`.

The local-host identification and the fixed-`Q` installed long-ear theorem
are independent gates.  Failure of the former is a type-mismatch
obstruction; success of the former leaves the quantitatively sharp second
gate stated in Section 5.
