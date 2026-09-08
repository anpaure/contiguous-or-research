# Parity complete mappings: an exact pair-clustered lift and its trace-code gate

Date: 2026-07-26

Method: pure mathematics only.

> **Support-tag correction (2026-07-26).**  The code
> `(J,x|J^c,p|J^c)` below is an augmented code: a literal lower or upper
> OR target does not in general determine `J`.  Thus noninjectivity of the
> augmented code is a valid literal collision obstruction, but augmented
> injectivity is not sufficient for literal target injectivity without a
> separate support-recovery theorem.  The same qualification applies to
> the half-step codes.

## 0. Outcome

The bounded-Lipschitz obstruction forces a typical Gaussian window to
complete \(\Theta(q)\) local direction pairs.  This note gives an exact
cycle construction which achieves that clustering while preserving every
middle owner.

Write the \(2r\) cube coordinates as ordered local pairs

\[
                         (a_i,b_i),\qquad i\in[r].                 \tag{0.1}
\]

Represent a cube vertex by

\[
 x_i=a_i,\qquad p_i=a_i\oplus b_i,                  \tag{0.2}
\]

so \(x\in Q_r\) is a phase vector and \(p\in Q_r\) is a local-parity
context.  Suppose that for every even \(p\) we have a neighbor permutation
\(F_p\) of \(Q_r\), with direction function \(d_p(x)\).

The exact lift condition is finite and pointwise:

\[
 \boxed{
 T_x:p\longmapsto p\oplus e_{d_p(x)}
 \text{ is a bijection }Q_r^{\rm even}\to Q_r^{\rm odd}
 \quad\text{for every }x.}                           \tag{0.3}
\]

Under (0.3), every coarse move lifts to the adjacent physical pair

\[
                         b_i, a_i,                                  \tag{0.4}
\]

and the result is one exact neighbor permutation of all \(Q_{2r}\).  If
every \(F_p\) is a physical \(C_{2r}\)-factor, the lift is a physical
\(C_{4r}\)-factor.  Every length-\(q\) window completes
\(\lfloor(q-1)/2\rfloor\) or more local pairs, exactly the scale required
by the transport theorem.

The context-independent choice \(F_p=F\) satisfies (0.3), but is unusable:
an aligned length-\(2d\) trace has multiplicity at least \(2^{d-1}\),
because it erases the parity bits on its \(d\) completed pairs.  Thus the
coarse order must genuinely depend on \(p\), and its completed-pair support
must encode the erased parity context.  The remaining target is the exact
simultaneous system (0.3) plus the trace codes in Section 4.

## 1. The exact lift

Let

\[
 E=\{p\in Q_r:|p|\equiv0\pmod2\},\qquad
 O=\{p\in Q_r:|p|\equiv1\pmod2\}.                    \tag{1.1}
\]

For each \(p\in E\), let \(F_p:Q_r\to Q_r\) be a permutation which moves
along one cube edge:

\[
                         F_p(x)=x\oplus e_{d_p(x)}.    \tag{1.2}
\]

Assume (0.3).  Define \(\widetilde F\) on \(Q_{2r}=Q_r^p\times Q_r^x\)
as follows.

For \(p\in E\), put \(i=d_p(x)\) and set

\[
 \widetilde F(p,x)=(p\oplus e_i,x).                  \tag{1.3}
\]

For \(p'\in O\), let \(p=T_x^{-1}(p')\), put \(i=d_p(x)\), and set

\[
 \widetilde F(p',x)=(p,F_p(x)).                      \tag{1.4}
\]

In physical bits, (1.3) toggles \(b_i\), while (1.4) toggles \(a_i\).

### Theorem 1.1 (parity complete-mapping lift)

The map \(\widetilde F\) is a neighbor permutation of \(Q_{2r}\), and

\[
                         \widetilde F^{,2}(p,x)=(p,F_p(x))
 \qquad(p\in E).                                      \tag{1.5}
\]

Conversely, for a lift of the form (1.3)--(1.4) to be a permutation, every
map (T_x) in (0.3) must be bijective.

#### Proof

For fixed (x), equation (1.3) maps the even contexts to the odd contexts
by (T_x), so it is bijective exactly under (0.3).  Equation (1.4) is its
unique inverse routing at the odd layer, followed by the bijection (F_p)
inside each recovered even context.  Hence every vertex has one successor
and one predecessor.  Both displayed moves toggle one physical bit, and
their composition is (1.5).  The same argument proves necessity of
bijectivity of (T_x). \(\square\)

Condition (0.3) says that, at every phase (x), the selected directions
(d_p(x)) form a perfect matching from the even to the odd shore of the
parity cube.  It is the exact local integrality equation; no rounding is
hidden in the lift.

## 2. Physical cycle structure and pair clustering

Assume every cycle of every (F_p) has length (2r), is isometric, and has
direction word (\pi\pi) for a permutation (\pi) of ([r]).

### Theorem 2.1 (exact pair-clustered physical factor)

Every cycle of (\widetilde F) has length (4r), is isometric in (Q_{2r}),
and has physical direction word

\[
 (b_{\pi_1},a_{\pi_1},\ldots,b_{\pi_r},a_{\pi_r})
 (b_{\pi_1},a_{\pi_1},\ldots,b_{\pi_r},a_{\pi_r}).   \tag{2.1}
\]

Consequently every cyclic window of (q) physical transitions completes at
least

\[
                         \left\lfloor\frac{q-1}{2}\right\rfloor \tag{2.2}
\]

local direction pairs.

#### Proof

Equation (1.5) identifies the even-time subsequence with one (F_p)-cycle,
so its length doubles from (2r) to (4r).  Each coarse direction (i) is
expanded as (b_i,a_i), giving (2.1).  The first (2r) physical moves use
every one of the (2r) directions exactly once, and the second half repeats
them.  Hence no arc of at most (2r) moves repeats a direction, which proves
isometry.  In a word partitioned into adjacent two-letter blocks, a cyclic
(q)-window loses at most one incomplete block at each boundary, proving
(2.2). \(\square\)

If every active local cell has middle rank two, a completed local pair has
lower rank zero and upper rank four.  Thus

\[
 Z(U)-Z(L)=2d\ge 2\left\lfloor\frac{q-1}{2}\right\rfloor,       \tag{2.3}
\]

so Theorem 2.1 meets the (\Omega(\sqrt m))-per-window transport scale at
(q=\Theta(\sqrt m)).

## 3. The context-independent lift is exactly too degenerate

Take one neighbor permutation (F) and put (F_p=F) for every even (p).
Then (d_p(x)=d(x)) is independent of (p), and

\[
                         T_x(p)=p\oplus e_{d(x)}       \tag{3.1}
\]

is a bijection.  Hence Theorem 1.1 gives an exact physical factor.

Fix an aligned physical window of length (2d) beginning at an even-time
state.  Let (J\subseteq[r]) be its (d) completed coarse directions.  Its
lower trace is empty on both physical coordinates of every (i\in J), and
its upper trace is full there.  On (J^c), either trace records the physical
orientation and therefore records both (x|_{J^c}) and (p|_{J^c}).

The coarse direction set (J) and (x|_{J^c}) may recover (x|_J) if (F) is
coarse-shadow injective.  They contain no information about (p|_J).

### Theorem 3.1 (exponential parity collision)

For every (d\ge1), every aligned depth-(2d) physical trace in the
context-independent lift has multiplicity at least

\[
                         \boxed{2^{d-1}}.              \tag{3.2}
\]

This holds for both lower and upper traces.

#### Proof

Fix the trace, hence (J), (x), and (p|_{J^c}).  Among assignments to the
(d) erased bits (p|_J), exactly (2^{d-1}) have the parity required to make
the full vector (p) even.  The successor rule and its coarse direction
word are independent of (p), so every one of those starts has the same
physical trace. \(\square\)

There are (2^{2r-1}) even-time starts.  Grouping them by their aligned
trace therefore leaves at most

\[
                         2^{2r-d}                    \tag{3.3}
\]

distinct aligned traces, and gives collision excess at least

\[
                         2^{2r-1}-2^{2r-d}.           \tag{3.4}
\]

For (d\to\infty) this is asymptotically one half of the entire cell, so
the failure is linear even before different outer packets interact.

At Gaussian depth (d=\Theta(\sqrt m)), this is exponential in
(\sqrt m).  Thus pair clustering alone and exact ownership are not close
to enough; the pair-block order must carry the erased context.

## 4. The exact context-code target

For an even context (p), phase (x), and coarse depth (d), let

\[
 J_{p,d}(x)=
 \{d_p(x),d_p(F_px),\ldots,d_p(F_p^{d-1}x)\}.          \tag{4.1}
\]

For aligned even-time windows, define the augmented code

\[
 \boxed{
 \mathcal C_d(p,x)=
 \big(J_{p,d}(x),\ x|_{J_{p,d}(x)^c},\
                    p|_{J_{p,d}(x)^c}\big).}          \tag{4.2}
\]

Therefore injectivity of (\mathcal C_d) is necessary for physical trace
injectivity: two starts with the same augmented code certainly have the
same literal target.  The converse is false in general because targets
with different `J` can coincide.  Conditional on `J` being intrinsically
recoverable at the outer interface, (4.2) has the exact interpretation:

> the context-dependent completed-pair support must recover the parity
> bits which that support erases.

Odd-time and odd-length windows add one or two partial boundary pairs.
Their augmented codes are obtained by adjoining the boundary roles and
retained endpoints to the full coarse envelope.  No new ownership equation
appears.  A raw target need not reveal those roles.

### Context-coded paired-order factor (open finite theorem)

Construct neighbor permutations (F_p), (p\in E), such that

1. every (F_p) is a (C_{2r})-factor with a doubled-permutation direction
   word;
2. the parity complete-mapping equations (0.3) hold for every (x);
3. the aligned codes (4.2) and both half-step codes are injective, or have
   total collision excess (o(2^{2r})) simultaneously for every protected
   depth; and
4. the resulting options can be coupled across the canonical outer packets
   with (o(W)) physical target deficit.

Items 1--3 are one finite recursion identity on (Q_r); item 4 is the outer
component-Hall coupling.  Theorems 1.1--3.1 show sharply why both pieces
are present: (0.3) solves exact ownership, adjacent expansion solves the
Gaussian transport magnitude, and only the context code can prevent the
resulting erased-parity collisions.
