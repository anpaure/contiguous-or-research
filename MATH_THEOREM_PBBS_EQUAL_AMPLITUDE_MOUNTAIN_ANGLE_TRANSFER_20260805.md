# Equal-amplitude mountain blocks give a q2-neutral angle transfer

**Date:** 2026-08-05  
**Method:** rooted PBBS factorization and a factorwise `A_1` KKR scan; no
computation or search  
**Status:** unconditional for `h>=t+3`, `t>=1`, `u,v>=1`, and
`u+v>=3`.  This extends the equal-height leaf transfer from amplitude one
to every amplitude `t` on the repeated-mountain face.  Arbitrary rigging
configurations at amplitude `t` remain a separate lifting problem.

## 1. Literal common-pivot family

Put

\[
 s=u+v,qquad m=h+ts+1,qquad n=2m+1,
\tag{1.1}

and use the deficit-three block word

\[
 0_{a_0}(1^t0^t)^u\;
 0_{a_1}(1^t0^t)^v\;
 0_{a_2}(1^h0^h).
\tag{1.2}

Let `c,d` be the first two down-steps of the height-`h` mountain.  Define
the complementary core `K` and the six clean-C6 shores by

\[
 R_i=K+a_i,quad P_i=K+a_i+a_{i+1},quad
 Q_i=K+a_i+c,quad L_i=P_i-d.
\tag{1.3}

The three normalized centers are

\[
\begin{aligned}
 A&=M_h\,1(M_t)^u0\,(M_t)^v,\\
 B&=(M_t)^u\,1(M_t)^v0\,M_h,\\
 C&=(M_t)^v\,1M_h0\,(M_t)^u,
\end{aligned}
\tag{1.4}

where `M_j=1^j0^j`.  Their dominant heights are `h,h,h+1`, and all
competitors have height at most `t+1`.  The first mountain down-step is
therefore the common reverse survivor `c`, so the centered factor contains
the three old shores `P_iQ_i`.

The three predecessor words have dominant heights `h+1,h,h`; every later
piece has height at most `t+2`.  Under `h>=t+3`, the second mountain
down-step is their common reverse survivor `d`.  Consequently

\[
                         P_i\cap f^{-2}(P_i)=P_i-d=L_i.
\tag{1.5}

The switch `P_iQ_i -> P_iQ_(i+1)` is therefore q1-exact,
upper-q1-exact, and q2-multiset-exact.

## 2. The repeated action profile

Peak pruning gives

\[
 \lambda(A)=\lambda(B)=(h,t+1,t^{s-1}),
 \qquad
 \lambda(C)=(h+1,t^s).
\tag{2.1}

Their top gaps are at least two.  Hence every required old and companion
occurrence is uniquely max-height selected.

## 3. Exact amplitude-`t` riggings

For the repeated profile in (2.1), the vacancy of a length-`t` string is

\[
                         q=2(h-t)+3.
\tag{3.1}

Run the highest-path KKR algorithm factorwise.  Scanning `M_h` creates one
length-`h` string.  Appending a ground factor `M_t` creates a new
length-`t` string without changing the `t`-vacancy.  Wrapping `u` ground
factors as

\[
                         1(M_t)^u0
\tag{3.2}

creates `u` singular `t`-strings at one common rigging and extends one of
them to length `t+1` at the terminal ball.

The resulting length-`t` rigging multisets are exactly

\[
\begin{aligned}
 J_t(A)&=\{(q-2)^{u-1},(q-1)^v\},\\
 J_t(B)&=\{0^u,1^{v-1}\}.
\end{aligned}
\tag{3.3}

The proof is the same vacancy ledger at scale `t`: a ground `M_t` changes
the word length by `2t` and `Q_t` by `t`, so it leaves `p_t` unchanged;
the leading and terminal wrapper letters raise it by two in total.  The
terminal letter promotes one singular `t`-string and leaves all others at
their displayed riggings.  The final mountain in `B` starts a fresh long
string after its leading empty run and does not alter the old
`t`-riggings.

## 4. Angle separation and transfer

The cyclic gap necklace of the repeated `t`-riggings is invariant under
all periodic action-angle slides.  From (3.3), for `u,v>=2` the two
necklaces are

\[
 (0^{u-2},1,0^{v-1},q-1),
 \qquad
 (0^{u-1},1,0^{v-2},q-1).
\tag{4.1}

They are unequal because their unique entries `1` and `q-1` delimit
different zero-run lengths.  The one-sided cases have respectively one
positive gap `q` versus two positive gaps `1,q-1`, and are also unequal.
Only `u=v=1` collapses to the one-string necklace `(q)`.

### Theorem 4.1

For `u+v>=3`, the equal-action centers `A,B` lie on different PBBS action
tori.  The third center has a different action partition.  Thus the clean
C6 in Section 1 is a genuine three-component q2-neutral merger.

For fixed `s`, varying `u` transfers one zero gap at a time between the two
distinguished arcs of the amplitude-`t` rigging necklace.  Hence the
repeated-height boundary of the profile descent has a literal angle-level
generator at every amplitude.

This family covers the two-cluster face of the amplitude-`t` necklace
space.  A full profile-descent forest still requires the corresponding
local transfer around every pair of adjacent nonzero gaps in an arbitrary
rigging necklace.

