# Audit of the claimed zero-winding converse and RP_A counterexample

Date: 2026-07-25

Pure mathematics only.  No computation or external input is used.

## 0. Verdict

The sector-shift Lemma 2.1 in
`PBBS_ZERO_WINDING_CONVERSE_AND_RPA_COUNTEREXAMPLE_20260725.md` is false.
Consequently its claimed classification

\[
d(D)=1\Longrightarrow
\text{next return gap }2\operatorname{ht}(D)+1
\]

is false as stated.  Explicit semilength-seven and primitive semilength-eight
counterexamples are given below.

The spectral Catalan estimate, long-cycle deletion, greedy quotient packing,
and \(N\)-fold deck amplification are correct **conditional on** a valid
short-return theorem for the primitive subfamily \(D=1E0\).  The second
counterexample below lies in that primitive subfamily, so the theorem needed
to activate those later estimates is itself false.  Thus the claimed
falsification of \((RP_A)\) is not established.

## 1. Where the sector shift fails

Along the first deepest spine, a forest \(A_i\) lies before the spine child
at depth \(i\).  Since the chosen leaf is first deepest, such a forest may
still have relative height exactly

\[
h-i-1.
\]

After a sector shift moves it one level deeper, it may reach total height
\(h\) before the displayed old spine.  Therefore the old displayed spine
need not remain the first deepest spine.  The proof in Lemma 2.1 controls
only the transported \(B_i\)-forests and omits this possibility.

A smallest transparent example is

\[
D=101100.
\]

It has height two and first-deepest sector \(A_0=10\).  Direct use of
\(\tau(P1R0S)=S1P0R\) gives

\[
\tau D=110100.
\]

In the transported display, the old \(A_0\)-leaf reaches height two before
the displayed continuation.  Thus the asserted first-deepest sector update
is already invalid after one shift.

## 2. Counterexample to the all-\(d=1\) converse

Let

\[
D_0=11100011110000.
\tag{2.1}
\]

This is a semilength-seven Dyck word, so \(N=15\).  Its first primitive
component has height three and its final primitive component has height
four.  Hence

\[
\operatorname{ht}(D_0)=4,
\qquad d(D_0)=1.
\tag{2.2}
\]

Repeatedly applying the exact block rotation gives the three-cycle

\[
\begin{aligned}
D_0&=11100011110000,\\
D_1&=11110001110000,\\
D_2&=11110000111000,\\
D_3&=D_0.
\end{aligned}
\tag{2.3}
\]

The first-maximum factorizations give

\[
\begin{array}{c|ccc}
 &D_0&D_1&D_2\\ \hline
d(D_j)&1&1&7\\
\delta(D_j)&10&4&4.
\end{array}
\tag{2.4}
\]

At the claimed return index \(s=h=4\),

\[
C_4=1+1+7+1=10,
\qquad
\delta(D_4)=\delta(D_1)=4.
\tag{2.5}
\]

These values are not equal and are not congruent modulo \(15\).  Therefore
the omitted coordinate does not return at gap

\[
2h+1=9.
\]

This disproves Theorem 3.1 and the advertised equivalence with \(d(D)=1\).

## 3. A primitive counterexample

The lower family used for the proposed \((RP_A)\) counterexample is

\[
\mathcal U_{r,A}=\{1E0:\operatorname{ht}(E)\le H-2\},
\]

which consists of primitive roots.  Even this restricted theorem is false.

First, the failure of the sector proof already appears in the primitive
root

\[
D=111001110000
\tag{3.1}
\]

has height four and \(B_0=\varnothing\).  Its successive roots begin

\[
\begin{aligned}
111001110000
&\mapsto111100110000\\
&\mapsto111100011000\\
&\mapsto111100001100.
\end{aligned}
\tag{3.2}
\]

Their deficits are

\[
1,1,1,5,
\tag{3.3}
\]

whereas the asserted sector formula with the original \(B_i\)'s empty
would give deficit one throughout the first four shifts.  This particular
word happens to return at gap nine, but the next primitive word does not.

Put

\[
\begin{aligned}
W_0&=1111000111100000,\\
W_1&=1111100011100000,\\
W_2&=1111100001110000,\\
W_3&=1111100000111000,\\
W_4&=1110001111100000.
\end{aligned}
\tag{3.4}
\]

Direct block rotation gives the five-cycle

\[
W_0\mapsto W_1\mapsto W_2\mapsto W_3\mapsto W_4\mapsto W_0.
\tag{3.5}
\]

The root \(W_2\) is primitive: after its initial five rises, its four
down-steps leave height one, its next three rises reach height four, and
only its final four down-steps return to zero.  Hence

\[
\operatorname{ht}(W_2)=5,
\qquad d(W_2)=1.
\tag{3.6}
\]

In the cycle order \((W_0,W_1,W_2,W_3,W_4)\),

\[
(d(W_i))=(1,1,1,7,1),
\qquad
(\delta(W_i))=(11,5,5,5,11).
\tag{3.7}
\]

Starting at \(W_2\), after the claimed \(s=h=5\) two-step moves one is
back at \(W_2\), but

\[
\sum_{j=0}^{4}d(\tau^jW_2)
=1+7+1+1+1=11,
\qquad
\delta(\tau^5W_2)=\delta(W_2)=5.
\tag{3.8}
\]

These are not congruent modulo \(N=17\).  Therefore \(W_2\) has no return
at gap \(11=2\operatorname{ht}(W_2)+1\).  The correct status is

\[
\boxed{
\text{primitive root}\Longrightarrow
\text{return at }2\operatorname{ht}+1
\quad\text{is false}.}
\tag{3.9}
\]

## 4. Correct recursive replacement for primitive roots

There is an exact recursion which explains the counterexample.  Let \(G(X)\)
denote the next omitted-coordinate return gap of a normalized PBBS root
\(X\).  If \(D\) is primitive and nontrivial, then

\[
F=\partial D
\]

is again primitive, and the terminal inverse slot in the lift \(F\mapsto D\)
is zero.  Since a primitive root has two-step deficit one, the reduced PBBS
starting at \(F\) has, after two updates,

\[
(u,F)\longmapsto(u-1,\tau F).
\tag{4.1}
\]

Thus the predecessor particle is selected for the first time at reduced
time two.  Its next selection occurs after an additional \(G(\tau F)\)
updates.  The exact terminal-spacing identity \(\Delta=1\) says that this
second predecessor selection is precisely the next outer physical return.
Consequently, whenever this time is below the outer circumference,

\[
\boxed{G(D)=2+G(\tau\partial D).}
\tag{4.2}
\]

In particular, since peak deletion lowers height by one and \(\tau\)
preserves height,

\[
G(D)=2\operatorname{ht}(D)+1
\]

holds exactly when \(\tau\partial D\) itself has the height-equality return.
The latter root need not be primitive.  This is the missing dynamic
condition which the false sector proof silently discarded.

## 5. Conditional audit of the Catalan mass

The following checks explain which later calculations would have been
correct had the primitive assertion been true.  Put

\[
H=\lceil A\sqrt r\rceil,
\qquad L=H-2.
\]

Then the number of proposed starts is exactly

\[
C_L(r-1),
\]

the number of semilength-\((r-1)\) Dyck paths of height at most \(L\).
The path-graph spectral formula is

\[
C_L(n)=\frac2{L+2}\sum_{j=1}^{L+1}
 \sin^2\!\frac{\pi j}{L+2}
 \left(2\cos\frac{\pi j}{L+2}\right)^{2n}.
\]

All terms are nonnegative.  Keeping \(j=1\), with
\(L=A\sqrt r+O(1)\), gives

\[
C_L(r-1)
\ge cA^{-3}r^{-3/2}4^{r-1}e^{-2\pi^2/A^2}
\ge c_A\operatorname{Cat}_r.
\]

Thus the fixed-Gaussian Catalan-positive mass estimate is correct.

## 6. Conditional audit of quotient and physical packing

Conditionally on the primitive return assertion, the quotient short-cycle
bound

\[
Z_H\le(2H+2)N^{2H+2}=\exp(o(r))=o(\operatorname{Cat}_r)
\]

is correct for fixed \(A\), since \(H=O(\sqrt r)\).  Therefore a positive
Catalan fraction of the starts lies on cycles longer than \(H+1\).

On one directed long cycle, an interval using at most \(H+1\) edges can
conflict only with starts in the preceding or following \(H\) positions.
Greedy selection loses at most \(2H+1\) starts and gives

\[
\overline\nu_H\ge c_A\frac{\operatorname{Cat}_r}{\sqrt r}.
\]

Every nonwrapping quotient interval has \(N=2r+1\) pairwise disjoint
spatial lifts, and lifts above quotient-edge-disjoint traces remain
disjoint.  Hence

\[
\nu_H(P_r)\ge N\overline\nu_H
\ge c_A\operatorname{Cat}_r\sqrt r.
\]

These normalizations and inequalities are correct.  But the primitive
short-return assertion is false, so they cannot be applied to the whole
family \(\mathcal U_{r,A}\).

## 7. Final status

The broad zero-winding converse in the supplied note is rigorously false.
Its proof has a precise first-deepest-spine error, and its primitive
restriction is also false.  The claimed failure of \((RP_A)\) therefore
does not follow.  A smaller primitive subfamily might still furnish a lower
obstruction, but its Catalan mass would require a new proof.
