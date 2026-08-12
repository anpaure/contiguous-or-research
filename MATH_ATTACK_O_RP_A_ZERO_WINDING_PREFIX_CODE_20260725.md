# Lane O: the exact zero-winding staircase field and its critical entropy ceiling

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
computation is used.

## 0. Outcome

Put

\[
 N=2r+1,
 \qquad B=\operatorname{Cat}_r,
 \qquad H_A=\lceil A\sqrt r\rceil,
\]

where \(A>0\) is fixed and \(r\to\infty\).  Let \(\tau=\phi^2\) be the
even-time PBBS quotient permutation on semilength-\(r\) Dyck words.  For

\[
 D_h=\tau^hD_0=P_h1R_h0S_h,
 \qquad d_h=|S_h|+1,
 \qquad \delta_h=|P_h|+1,
\]

the zero-winding equation is

\[
 \sum_{h=0}^{s-1}d_h=\delta_s.                    \tag{0.1}
\]

The main positive result of this note is the following exact literal
identity:

\[
 \boxed{
 P_s1=(S_{s-1}1)(S_{s-2}1)\cdots(S_01).}
                                                               \tag{0.2}
\]

Moreover,

\[
 \boxed{
 \operatorname{ht}(D_h)=s\quad(0\le h\le s),
 \qquad \operatorname{ht}(S_h)\le h\quad(0\le h<s).}
                                                               \tag{0.3}
\]

Thus every zero-winding return has an exact staircase prefix field.  If
\(C_h(z)\) counts Dyck words of height at most \(h\), its binary Kraft mass
is exactly

\[
 \boxed{
 \prod_{h=0}^{s-1}{C_h(1/4)\over2}
 =\prod_{h=0}^{s-1}{h+1\over h+2}
 ={1\over s+1}.}
                                                               \tag{0.4}
\]

The exact **field Kraft deficit** is \(\log _2(s+1)\) bits.  This is not yet
an injective shortening of the whole return: the terminal tail must still
be encoded, and a finite-length Catalan completion lemma would be needed to
promote the field deficit to a return-counting entropy gain.  The decisive
no-crossing step in (0.2) is independently audited by the strict
first-passage variable below; the later dual identities are consequences,
not an independent proof of (0.2).

This does **not** prove \(\mathrm{RP}_A\).  The quotient target is

\[
 \overline\nu_{H_A}=o_A(B/N).                       \tag{0.5}
\]

An edge-disjoint length-\(s\) interval supplies at most one further
length factor \(1/s\).  Even if a valid completion lemma promoted (0.4) to
a Catalan counting factor and that factor could then be multiplied
independently by the packing factor, restoring the \(N\)-fold spatial deck
would leave the critical multiplier

\[
 {N\over s(s+1)}.
                                                               \tag{0.6}
\]

For \(s=\lfloor a\sqrt r\rfloor\), with fixed \(a>0\),

\[
 \boxed{
 {N\over s(s+1)}\longrightarrow {2\over a^2},}
                                                               \tag{0.7}
\]

not zero.  Equivalently, the idealized completed staircase deficit plus
the optimistic packing entropy gives only

\[
 \log_2(s(s+1))=\log_2N+O_a(1),                    \tag{0.8}
\]

whereas (0.5) requires \(\log_2N+\omega(1)\) bits.  A further dynamic
factor tending to zero is indispensable.

There is a second, dual staircase whose enlarged formal capped language has
the same Kraft mass, but it cannot be multiplied with (0.4) without a new
correlation theorem.  An explicit family of \(F_{r-4}\) zero-winding roots
has initial and terminal
first-maximum prefixes both of length \(N-4\); any realization of those two
regions on the common \((N-1)\)-token word overlaps in at least \(N-7\)
tokens.  All but \(\exp(o(r))\) of these roots lie on
long quotient cycles, and each root retains \(\Omega(N)\) physically
edge-disjoint spatial translates.  Hence neither two-sided endpoint
lengths, long-cycle restriction, nor packedness justifies squaring (0.4).

The exact proved boundary is therefore:

* the exact fixed-\(s\) prefix-free staircase **field** exists and has Kraft
  deficit \(\log_2(s+1)\);
* no nontrivial injective shortening of the whole return is obtained merely
  by appending the still-uncontrolled terminal tail;
* even an ideal completion of that field deficit is critical, not little-oh,
  after the deck and interval ledgers;
* the missing theorem is a genuinely joint dynamic code or clustering
  statement contributing an additional \(\omega(1)\) bits after overlap.

No constant-one conclusion is claimed.

## 1. Quotient normalization and the literal recursion

For a Dyck word \(D\), mark the first up-step reaching its global maximum
and then the first subsequent down-step returning to height zero.  This
gives the unique factorization

\[
 D=P1R0S,                                           \tag{1.1}
\]

where \(S\) is Dyck.  The exact two-step PBBS quotient map is

\[
 \boxed{\tau D=S1P0R.}                              \tag{1.2}
\]

In particular, for \(D_h=\tau^hD_0\),

\[
 \boxed{
 P_{h+1}1R_{h+1}0S_{h+1}=S_h1P_h0R_h.}
                                                               \tag{1.3}
\]

The quotient map preserves Dyck height.  One quick proof is to use the
one-step formula

\[
 \phi(P1Q)=\overline Q\,0\,\overline P.
\]

If the marked step first reaches height \(t\), then \(\overline Q\), read
from zero, stays nonnegative and reaches height \(t\), while the remaining
word stays at or below \(t\).  Thus \(\phi\), and hence \(\tau\), preserves
height.

An omitted coordinate returns after \(2s+1\) PBBS steps with zero winding
exactly when (0.1) holds.  The \(s\) roots

\[
 D_0,D_1,\ldots,D_{s-1}                             \tag{1.4}
\]

are the deficit-carrying quotient edges.  For a quotient-edge-disjoint
family of nonwrapping intervals on the long quotient cycles, these deficit
cores are pairwise disjoint, and hence

\[
 \sum_{I\in\mathcal P}s(I)\le B.                   \tag{1.5}
\]

On long quotient cycles, every quotient interval has all \(N\) spatial
lifts, and lifts of quotient-edge-disjoint intervals are physically
edge-disjoint.  Therefore \(\mathrm{RP}_A\) requires (0.5).  A quotient
bound of merely \(o_A(B)\) is too weak by the full factor \(N\).

## 2. Strict no-crossing and the staircase identity

Define

\[
 L_h=\sum_{j=0}^{h-1}d_j,
 \qquad M_h=\delta_h-L_h.                           \tag{2.1}
\]

Thus \(L_0=0\), and zero winding says \(M_s=0\).

### Theorem 2.1 (strict first-passage variable)

For every \(0\le h<s\),

\[
 \boxed{M_h\ge s-h>0.}                              \tag{2.2}
\]

Consequently zero winding is automatically the first return: no proper
prefix gives either a zero- or a positive-winding congruence.

#### Proof

In

\[
 D_{h+1}=S_h1P_h0R_h,                               \tag{2.3}
\]

the path has reached its invariant global height by the end of \(P_h\).
Indeed, \(S_h\) has net height zero, the displayed one contributes one,
and \(P_h\) ends at height one below the maximum in \(D_h\).  The end of
\(P_h\) in (2.3) is at position

\[
 d_h+\delta_h-1.
\]

Since \(\delta_{h+1}\) is the *first* maximum-reaching position,

\[
 \delta_{h+1}\le d_h+\delta_h-1.                   \tag{2.4}
\]

Therefore

\[
 M_{h+1}
 =\delta_{h+1}-(L_h+d_h)
 \le M_h-1.                                         \tag{2.5}
\]

Iterating backward from \(M_s=0\) proves (2.2).

For \(h<s\), (2.2) gives \(L_h<\delta_h<N\).  An earlier return would
require

\[
 L_h=\delta_h+aN
\]

for some integer \(a\ge0\), which is impossible.  \(\square\)

### Theorem 2.2 (literal staircase prefix)

Put

\[
 Q_h=(S_{h-1}1)(S_{h-2}1)\cdots(S_01),
 \qquad Q_0=\varnothing.                            \tag{2.6}
\]

Then \(Q_h\) is the length-\(L_h\) prefix of \(P_h\) for \(h<s\), and

\[
 \boxed{Q_s=P_s1.}                                  \tag{2.7}
\]

Consequently (0.2)--(0.3) hold.

#### Proof

The assertion is empty at \(h=0\).  Suppose \(Q_h\) is the length-\(L_h\)
prefix of \(P_h\).  Equation (2.3) begins with

\[
 S_h1Q_h=Q_{h+1}.                                   \tag{2.8}
\]

For \(h+1<s\), Theorem 2.1 gives

\[
 |Q_{h+1}|=L_{h+1}<\delta_{h+1}=|P_{h+1}|+1.
\]

Thus this prefix ends before the marked first-maximum step and is the
length-\(L_{h+1}\) prefix of \(P_{h+1}\).  At the terminal induction step
\(h+1=s\), its length is

\[
 |Q_s|=L_s=\delta_s=|P_s|+1,
\]

so it is exactly \(P_s1\).  This proves (2.7).

Every block \(S_h\) has net height zero, and (2.7) contains exactly \(s\)
displayed up-steps.  Therefore \(P_s1\) ends at height \(s\).  Its last
symbol is the first attainment of the global maximum, so

\[
 \operatorname{ht}(D_s)=s.
\]

Height invariance gives \(\operatorname{ht}(D_h)=s\) for every \(h\).
In (2.7), the block \(S_h\) starts at height \(s-1-h\).  If it had height
at least \(h+1\), the path would reach height \(s\) before the final
displayed up-step.  Hence \(\operatorname{ht}(S_h)\le h\).  In particular,

\[
 S_0=\varnothing,
 \qquad d_0=1.                                      \tag{2.9}
\]

This proves all assertions.  \(\square\)

Theorem 2.1 is the independent audit of the potentially dangerous step in
Theorem 2.2: the block induction is legal because every proper accumulated
length lies *strictly* before the next marked maximum.  No unproved
``no overshoot'' assumption is being used.

## 3. The exact prefix-free staircase field

For fixed \(s\ge1\), let \(\mathcal L_s\) be the language

\[
 \mathcal L_s=
 \left\{
 (E_{s-1}1)(E_{s-2}1)\cdots(E_01):
 E_h\text{ Dyck and }\operatorname{ht}(E_h)\le h
 \right\}.                                         \tag{3.1}
\]

### Lemma 3.1 (unique first-passage parsing)

\(\mathcal L_s\) is exactly the set of nonnegative binary walks which
first reach height \(s\) at their last symbol.  Its displayed block
decomposition is unique.  In particular, \(\mathcal L_s\) is prefix-free.

#### Proof

A word in (3.1) starts the block \(E_h\) at height \(s-1-h\).  The height
cap keeps it below \(s\), and the following displayed one raises the
running floor by one.  Hence the final displayed one is the first hit of
height \(s\).

Conversely, in a nonnegative first-passage word to height \(s\), mark the
last departure from height zero, then the last departure from height one,
and so on.  The portions before these successive departures are Dyck
excursions based at the current level.  Before the departure from level
\(s-1-h\), the path remains below \(s\), so the corresponding excursion
has height at most \(h\).  This produces (3.1) uniquely.

If one member of \(\mathcal L_s\) were a proper prefix of another, the
longer word would already have reached height \(s\) before its last symbol,
a contradiction.  \(\square\)

For a zero-winding quotient return \(I=(D_0,s)\), one injective terminal
description is of course the terminal root itself,

\[
 \mathsf C(I)=D_s=Q_sR_s0S_s,                       \tag{3.2}
\]

with \(Q_s\in\mathcal L_s\).  This description is injective: after the fixed-length
terminal word is read, \(s\) is recovered as the height of \(D_s\), and
then \(D_0=\tau^{-s}D_s\).  At fixed semilength all codewords have length
\(2r\), so the full description is prefix-free but trivially unshortened.
Conditional on known \(s\), its
initial field is the prefix-free literal history \(Q_s\).  The union
\(\bigcup_s\mathcal L_s\) is not prefix-free (for example,
\(1\in\mathcal L_1\) prefixes \(11\in\mathcal L_2\)); this is precisely why
a global proof must account for the height wrapper rather than sum the
fixed-\(s\) Kraft gains for free.  In particular, Theorem 3.2 below is an
exact statement about this constrained field.  It is not, by itself, a
Catalan-normalized upper bound on the number of complete terminal roots.

### Theorem 3.2 (exact Kraft mass)

The fixed-\(s\) staircase field has exact binary Kraft mass

\[
 \boxed{
 \sum_{Q\in\mathcal L_s}2^{-|Q|}={1\over s+1}.}
                                                               \tag{3.3}
\]

#### Proof

Let \(C_h(z)\) count Dyck words of height at most \(h\), by semilength.
Thus

\[
 C_0(z)=1,
 \qquad
 C_h(z)={1\over1-zC_{h-1}(z)}.                     \tag{3.4}
\]

At \(z=1/4\), induction gives

\[
 \boxed{C_h(1/4)={2(h+1)\over h+2}.}                \tag{3.5}
\]

Indeed the formula is true for \(h=0\), and substituting the value for
\(h-1\) into (3.4) gives the value for \(h\).

For one block \(E_h1\),

\[
 \sum_{\operatorname{ht}(E_h)\le h}
 2^{-(|E_h|+1)}
 ={1\over2}C_h(1/4).
\]

The decomposition in Lemma 3.1 is unique, so multiplication and (3.5)
give

\[
 \sum_{Q\in\mathcal L_s}2^{-|Q|}
 =\prod_{h=0}^{s-1}{h+1\over h+2}
 ={1\over s+1}.
\]

\(\square\)

The value in (3.3) is exact, not an upper estimate.  It is useful also as
a warning: the staircase language is the *entire* first-passage language.
Appending every legal continuation from height \(s\) back to zero, without
exceeding \(s\), gives precisely all semilength-\(r\) Dyck words of height
exactly \(s\).  Hence (3.3) by itself encodes no return-specific rarity
beyond the proved equality \(\operatorname{ht}(D)=s\).

## 4. The fixed-length scalar saving and why it is paid back

If one temporarily forgets the individual height caps and retains only the
scalar equation, a formal history of total staircase length \(L\) is an
\(s\)-tuple of Dyck words satisfying

\[
 \sum_{h=0}^{s-1}(|S_h|+1)=L.                      \tag{4.1}
\]

Let \(C(z)\) be the unrestricted Catalan generating function.  If
\(L\equiv s\pmod2\), then the exact number of such histories is

\[
 \boxed{
 \left[z^{(L-s)/2}\right]C(z)^s
 ={s\over L}\binom{L}{(L-s)/2}.}                  \tag{4.2}
\]

It is zero for the other parity.

For \(s=x\sqrt L+O(1)\), where \(x\) stays in a fixed compact subset of
\((0,\infty)\), Stirling's formula gives

\[
 \log_2\left(
 {s\over L}\binom{L}{(L-s)/2}
 \right)
 =L-\log_2L+O_x(1).                                \tag{4.3}
\]

Thus fixing \((L,s)\) appears to save the deck-scale quantity
\(\log_2L+O(1)\).  That saving is not a free global gain.  The terminal
length is \(L=\delta_s\), which ranges over \(\Theta(r)\) possible values.
After the actual first-maximum caps are restored and all lengths are
allowed, the exact aggregate mass is (3.3), only \(1/(s+1)\).  Equivalently,
making \(L\) self-delimiting costs the logarithmic saving visible in
(4.3).

There is also a literal ambiguity obstruction to deleting the separators.
Take

\[
 S_h=(10)^{j_h},
 \qquad j_h\ge0,
 \qquad \sum_{h=0}^{s-1}j_h=J.                    \tag{4.4}
\]

After the separators are removed, every one of these histories becomes
the same word \((10)^J\), while the number of histories is

\[
 \boxed{\binom{J+s-1}{s-1}.}                       \tag{4.5}
\]

Hence the literal delimiter-free encoding of these formal scalar histories
is not injective and cannot retain the local \(\log L\) saving.  These
tuples were defined after forgetting the height caps and are not asserted
to be dynamically realizable zero-winding histories; (4.5) does not rule
out a different joint dynamic code.

## 5. The critical entropy ledger

The physical PBBS factor has \(NB\) rooted states, while \(\mathrm{RP}_A\)
asks for a physical packing of size \(o_A(B)\).  Equivalently, after the
deck reduction, the quotient packing must be \(o_A(B/N)\).  A direct
global encoding of quotient starts therefore needs a reduction factor

\[
 N\omega_A(r),
 \qquad \omega_A(r)\longrightarrow\infty,          \tag{5.1}
\]

or an entropy gain

\[
 \log_2N+\omega(1).                                \tag{5.2}
\]

The staircase field has exact Kraft deficit \(\log_2(s+1)\).  A separate
completion lemma would have to convert that field deficit into a comparable
finite-length Catalan saving.  The raw disjoint-edge budget (1.5) can
contribute at most the length factor \(s\), i.e. at most another
\(\log_2s\) bits.  Even granting both the completion step and a
tensorization with packing, their combined gain is

\[
 \log_2(s(s+1)).                                   \tag{5.3}
\]

At the Gaussian scale \(s=a\sqrt r+O(1)\), (0.7)--(0.8) show that (5.3)
is only \(\log_2N+O_a(1)\).  It can prove at best a constant multiple of
the Catalan target after the deck, never a little-oh.

This is an *optimistic ceiling*, not an achieved code length.  In general, a rarity estimate and an
edge-packing estimate combine by a minimum, not a product.  Multiplying
them itself requires an injective capacity or tensorization lemma.  Thus
the exact conclusion is stronger than merely observing that the presently
written proof is loose: even the favorable independent-product ledger is
critical.

A sufficient new input would be either

1. a global Catalan-normalized code for all long-cycle zero-return starts
   of total mass \(o_A(1/N)\); or
2. a valid joint code/capacity theorem which, after the staircase and
   interval factors, contributes a further factor
   \(\eta_{r,A}\to0\).

In bits, the second alternative is precisely an additional
\(-\log_2\eta_{r,A}=\omega(1)\).  If the proof is summed over dyadic length
bands using only a worst-case bound in each band, the additional gain must
also pay the number of retained bands; a global prefix code can avoid that
wrapper.

## 6. The exact dual staircase

The strict variable \(M_h\) supplies a second literal factorization.  Put

\[
 e_h=M_h-M_{h+1}
 =\delta_h+d_h-\delta_{h+1}\ge1.                   \tag{6.1}
\]

### Theorem 6.1 (dual staircase and local seam identity)

For each \(0\le h<s\), there is a Dyck word \(T_h\) such that

\[
 e_h=|T_h|+1,
 \qquad \operatorname{ht}(T_h)\le s-1-h,           \tag{6.2}
\]

and

\[
 \boxed{S_h1P_h=P_{h+1}1\overline{T_h},}           \tag{6.3}
\]

\[
 \boxed{\overline{T_h}0R_h=R_{h+1}0S_{h+1}.}       \tag{6.4}
\]

Consequently

\[
 \boxed{
 P_01=(\overline{T_{s-1}}1)
      (\overline{T_{s-2}}1)\cdots
      (\overline{T_0}1),}                          \tag{6.5}
\]

and

\[
 \boxed{
 (\overline{T_{s-1}}0)\cdots(\overline{T_0}0)R_0
 =R_s(0S_s)(0S_{s-1})\cdots(0S_1).}                \tag{6.6}
\]

The ambient formal language obtained by allowing every tuple satisfying the
caps in (6.2) has exact Kraft mass \(1/(s+1)\).  The dynamically realized
dual tuples form a subset, so their Kraft mass is at most this value.

#### Proof

In \(D_{h+1}=S_h1P_h0R_h\), consider the subword after the first
maximum-reaching bit through the end of \(P_h\).  It has length

\[
 d_h+\delta_h-1-\delta_{h+1}=e_h-1.                \tag{6.7}
\]

It starts and ends at the global height \(s\) and never rises above it.
Its complement is therefore a Dyck word; call it \(T_h\).  This proves
(6.2) except for the height cap, and the literal split gives (6.3).

Substituting (6.3) into the two factorizations of \(D_{h+1}\) gives
(6.4).  Iterating (6.3), then using (0.2), gives

\[
 \begin{aligned}
 &(S_{s-1}1)\cdots(S_01)P_0\\
 &\qquad=P_s1(\overline{T_{s-1}}1)
                \cdots(\overline{T_1}1)\overline{T_0}.
 \end{aligned}
\]

The common prefix on the two sides is \(P_s1\), so cancellation proves
(6.5).  Since \(P_01\) first reaches height \(s\) at its last symbol, the
block \(\overline{T_h}\), which begins at height \(s-1-h\), may descend
by at most that amount.  This is exactly the cap in (6.2).

Iterating (6.4) proves (6.6).  Finally, complementation does not change
length, and the caps in (6.2) are the same set \(0,1,\ldots,s-1\) in
reverse order.  The calculation in Theorem 3.2 therefore gives the exact
mass \(1/(s+1)\) for the enlarged formal capped language, and an upper bound
of that size for its dynamically realized sublanguage.  \(\square\)

The dual identity is genuine additional structure, but its entropy cannot
simply be added to the forward entropy.  Both ladders are deterministic
functions of the same root, and \(D_s=\tau^sD_0\).  A joint injection must
control their overlap or conditional multiplicity.  The next section
shows that no universal disjoint-token interpretation is possible.

## 7. Audited disjoint-token obstruction

### Theorem 7.1 (exponentially many long-cycle maximal endpoint lengths)

Let \(r\ge5\), put \(N=2r+1\), and use the two Dyck blocks

\[
 \mathsf A=1100,
 \qquad \mathsf B=10.                               \tag{7.1}
\]

Let \(U\) be an arbitrary word in the block alphabet
\(\{\mathsf A,\mathsf B\}\) of total semilength \(r-5\), and put

\[
 V=\mathsf A U,
 \qquad
 D_0=V111000.                                       \tag{7.2}
\]

Then the first three quotient iterates are

\[
 \boxed{
 \begin{aligned}
 D_1&=1V11000,\\
 D_2&=111000\,U\mathsf A,\\
 D_3&=U\mathsf A\,111000.
 \end{aligned}}                                    \tag{7.3}
\]

Starting at \(D_0\), there is a genuine first zero-winding return with
\(s=3\), and

\[
 \boxed{\delta_0=\delta_3=N-4.}                    \tag{7.4}
\]

Consequently

\[
 \boxed{
 \delta_0+\delta_3-(N-1)=N-7.}                    \tag{7.5}
\]

There are exactly \(F_{r-4}\) choices of \(U\), where
\(F_0=0,F_1=1,F_{j+1}=F_j+F_{j-1}\).  For every fixed \(A>0\), all but
\(\exp(o(r))\) of the resulting roots lie on quotient \(\tau\)-cycles of
length greater than \(H_A+1\).

#### Proof

Every block word \(U\) is Dyck of height at most two.  The exact
first-maximum factorizations along (7.3) are

\[
 \begin{aligned}
 D_0&=(V11)1(00)0,\\
 D_1&=(11)1(00\,U\mathsf A)0,\\
 D_2&=(11)1(00)0(U\mathsf A).
 \end{aligned}                                      \tag{7.6}
\]

Applying \(\tau(P1R0S)=S1P0R\) successively gives (7.3).  The relevant
suffixes are

\[
 S_0=S_1=\varnothing,
 \qquad S_2=U\mathsf A.                             \tag{7.7}
\]

The word \(U\mathsf A\) has the same length as \(V\), namely

\[
 |V|=2(r-3)=N-7.
\]

Therefore

\[
 d_0+d_1+d_2
 =1+1+(|V|+1)
 =N-4.                                              \tag{7.8}
\]

The first maximum in \(D_3=U\mathsf A111000\) is the last up-step of the
terminal mountain, so

\[
 \delta_3=|U\mathsf A|+3=N-4.                      \tag{7.9}
\]

This proves zero winding and (7.4).  The two proper accumulated sums are
\(1<\delta_1=3\) and \(2<\delta_2=3\), so it is the first return.  Equation
(7.5) follows from \(N-1=2r\).

A block word \(U\) is the same thing as a composition of \(r-5\) into
parts one and two.  The number of these is \(F_{r-4}\), proving the exact
count.  Finally, the standard voltage-itinerary bound gives at most

\[
 (2H_A+2)N^{2H_A+2}=\exp(o(r))                     \tag{7.10}
\]

Dyck roots on quotient \(\tau\)-cycles of length at most \(H_A+1\), since
\(H_A\log N=o(r)\).  As \(F_{r-4}=\exp(\Theta(r))\), all remaining roots
in the displayed family lie on long cycles.  \(\square\)

For every member of the family, the forward staircase is

\[
 (S_21)(S_11)(S_01)=(U\mathsf A)111=P_3\,1.        \tag{7.11}
\]

The length calculation has the following exact coding scope: if both
endpoint certificate regions are allocated inside one common
\((N-1)\)-token store, pigeonhole forces them to reuse at least \(N-7\)
tokens.  This is not a claim that two native physical-coordinate arcs have
intrinsic intersection \(N-7\); those arcs live in an \(N\)-coordinate
ground and require a separate phase convention.  In general Theorem 2.2
gives only

\[
 s\le\delta_h\le N-1-s,                            \tag{7.12}
\]

because the first hit of height \(s\) needs at least \(s\) steps and the
return from height \(s\) needs at least \(s\) further steps.  The family
above attains the upper endpoint in (7.12) at both \(h=0\) and \(h=s\).
Therefore endpoint lengths cannot supply a disjoint-token proof, even after
the short quotient cycles are removed.  This does not refute a different
joint Kraft or conditional-rarity inequality.

### Proposition 7.2 (packedness does not remove the disjoint-token obstruction)

For each return in Theorem 7.1, its \(N\) spatial translates contain a
pairwise physically edge-disjoint subfamily of size at least \(N/25\).

#### Proof

After repeated entries, if any, are discarded, the lifted projected support
contains at most five physical edges.  Fix one spatial translate.  Another
translate can meet it only if one of its at most five support edges is
translated onto one of the fixed support edges.

The coordinate-rotation action is free on physical PBBS edges.  Indeed, if
a nontrivial rotation fixed an endpoint \(r\)-set, its coordinate orbits
would have a common size \(q>1\) dividing both \(N\) and \(r\), impossible
because \(\gcd(N,r)=1\).  A rotation cannot stabilize an unordered edge by
swapping its endpoints: its square would fix each endpoint, and every
rotation has odd order dividing \(N\), so the square generates the same
nontrivial subgroup.

Thus each ordered pair of support edges forbids at most one relative
translation.  There are at most \(5^2-1=24\) conflicting nontrivial
translations.  The conflict graph on the \(N\) translates has maximum
degree at most \(24\), and greedy independent-set selection gives at least
\(N/25\) vertices.  \(\square\)

The whole constructed family has
\(F_{r-4}=\Theta(\varphi^r)\), where
\(\varphi=(1+\sqrt5)/2<4\), and the spatial deck contributes only a
polynomial factor.  It is therefore **not** a counterexample to
\(\mathrm{RP}_A\).  Its exact scope is narrower and decisive for the
coding proposal: neither long-cycle restriction, local packedness, nor
endpoint lengths supplies a disjoint-token proof that the two
\(1/(s+1)\) Kraft factors multiply.

Time reversal does not repair this automatically.  If the forward
\((2s+1)\)-step one-step voltages sum to \(sN\), reversing the same edges
while retaining the same clockwise ground orientation gives voltage sum

\[
 (2s+1)N-sN=(s+1)N.                                \tag{7.13}
\]

Thus a reverse zero-winding argument must explicitly reverse the ground
orientation; it is not a second copy of the forward scalar equation in the
same coordinates.

## 8. Final proved and conditional boundary

The exact zero-winding equation has now been converted into a literal,
uniquely parsed fixed-\(s\) prefix field.  Its decisive properties are:

\[
 \begin{array}{c|c}
 \text{property}&\text{proved value}\\ \hline
 \text{forward staircase Kraft mass}&1/(s+1)\\
 \text{forward field Kraft deficit}&\log_2(s+1)\\
 \text{raw edge-packing factor}&\le1/s\\
 \text{Gaussian deck ratio}&N/[s(s+1)]\to2/a^2\\
 \text{formal dual-language Kraft mass}&1/(s+1)\\
 \text{realized dual-language Kraft mass}&\le1/(s+1)\\
 \text{forward/dual disjoint-token derivation}&\text{refuted}\\
 \text{general joint tensorization}&\text{unproved.}
 \end{array}                                       \tag{8.1}
\]

Therefore the route closes only after a quantitatively adequate new
statement is proved.  One precise bandwise version is the following.  Let
\(t\) range over dyadic integers covering the part of \([1,H_A]\) not
already removed by the sub-Gaussian height theorem.

> **Joint conditional-entropy/capacity lemma — UNPROVED.**  There are
> factors \(\eta_{r,A}(t)\) and a valid single global completion code, or an
> equivalent capacity tensorization, such that the physical contribution
> of packed long-cycle zero returns with \(t\le s<2t\) is at most
> \[
> C_A B\,\eta_{r,A}(t){N\over t^2},
> \]
> and
> \[
> \sum_t\eta_{r,A}(t){N\over t^2}=o_A(1).
> \]

At a genuinely Gaussian scale \(t\asymp\sqrt r\), this asks for
\(\eta_{r,A}(t)\to0\).  In a lower mesoscopic band it correctly asks for
the stronger gain needed to compensate \(N/t^2\); a bare uniform
\(\eta_{r,A}\to0\) is not sufficient over the entire window.

A wrapper-free sufficient global target is:

> **Packed dynamic-code lemma — UNPROVED.**  There is one global injective
> encoding of the members of every packed long-cycle quotient zero-return
> family into binary strings of length at most
> \[
> \log_2(B/N)-\gamma_{r,A},
> \qquad \gamma_{r,A}\longrightarrow\infty.
> \]
> The same code book is used for the entire family; hence the number of
> available strings, and therefore the quotient packing, is \(o_A(B/N)\).

Either formulation supplies the missing aggregate entropy.  The scalar
equation, first-return condition, one staircase field, the raw packing
budget, and the endpoint-dual staircase do not.  Proving one of these joint
statements, or a different cross-orbit clustering theorem at the same
\(o_A(B/N)\) scale, remains the sole unresolved boundary in this lane.
