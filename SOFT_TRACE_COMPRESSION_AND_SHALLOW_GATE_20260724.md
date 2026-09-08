# Soft trace compression and the shallow central-trace gate

## Verdict

The marked-coordinate trace-compression theorem is correct.  Its proof can
be sharpened in two independent ways:

1. only the **number of intermediate-trace holes** has to be small; the
   weighted defect `Delta` is a sufficient but nonminimal surrogate;
2. after the random cyclic-order reservoir, this condition is needed only
   through depth `(1+o(1)) sqrt(m log log m)`, and the shallow base family
   need not be an exact middle factor.

All constructions below are literal words of nonempty masks, so there is no
separate factorability, linked-band, lower-core, or pin-survival condition.

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad N_q=\binom n{m-q}.
\]

## 1. Exact trace-compression inequality

Let `P` be a multiset of `p` cyclic orders.  For `0<=q<=h`, let
`H_q(P)` be the rank-`m-q` masks absent from their length-`m-q` cyclic
intervals.  Fix a marked set `Z` of size `t` and an integer `0<=a<t/2`.
Define

\[
G_{h,a}(P,Z)=
 \sum_{q=0}^{h}
 \left|\left\{S\in H_q(P):
 a<|S\cap Z|<t-a\right\}\right|.
\tag{1.1}
\]

Let `R_ext` be the number of distinct traces needed by the remaining holes
and their complements.  Then

\[
R_{\rm ext}\le 2\sum_{j=0}^{a}\binom tj.
\tag{1.2}
\]

### Theorem 1 (exact central-trace compression)

The ranks at depths `0,...,h` on both sides of the middle have a literal
contiguous-OR word of length at most

\[
p(n+2h+1)
  +2G_{h,a}(P,Z)
  +R_{\rm ext}\bigl(\nu(n-t)+1\bigr).
\tag{1.3}
\]

### Proof

Emit the depth-`h` erosion block for every cyclic order in `P`.  Its
consecutive unions give every cyclic interval on both sides through depth
`h`, and the total base length is `p(n+2h+1)`.

For a fixed trace `R subseteq Z`, put `X=[n] minus Z` and take a universal
word `V_1,...,V_(nu(n-t))` on `X`.  If `R` is empty, use this word.  If it is
nonempty, use

\[
R,\quad R\cup V_1,\ldots,R\cup V_{\nu(n-t)}.
\]

This one block covers every nonempty mask whose trace on `Z` is exactly
`R`, in every rank.  A lower hole with trace `R` has complementary upper
hole with trace `Z minus R`.  Hence one block for every distinct extreme
trace occurring among the holes or their complements repairs every hole
with trace size at most `a` or at least `t-a`.  The number of possible
blocks is bounded by (1.2).

Exactly the holes counted by (1.1) remain.  Append each and its complement
literally, at cost `2G_(h,a)`.  This proves (1.3).  `square`

The user's weighted defect

\[
\Delta_h(P,Z)=
 \sum_{q=0}^{h}\sum_{S\in H_q(P)}|Z\setminus S|
\]

satisfies

\[
G_{h,a}(P,Z)\le \Delta_h(P,Z)/(a+1),
\]

so the displayed weighted theorem follows.  But (1.3) shows that extreme
holes should not be charged at all; they have already been compressed.

## 2. Optimal asymptotic placement of the trace cut

Assume `t->infinity` and `t=o(n)`.  The unconditional upper bound
`nu(d)=O(W(d))` and the central-width ratio give

\[
\frac{R_{\rm ext}(\nu(n-t)+1)}{W(n)}
 =O\!\left(2^{-t}\sum_{j=0}^{a}\binom tj\right)+o(1).
\tag{2.1}
\]

Thus it is enough that

\[
2^{-t}\sum_{j=0}^{a}\binom tj=o(1).
\tag{2.2}
\]

A fixed cut `a=floor(alpha t)`, `alpha<1/2`, works.  A sharper choice is

\[
a=\left\lfloor t/2-b(t)\right\rfloor,
\qquad \sqrt t\ll b(t)=o(t).
\tag{2.3}
\]

Hoeffding gives

\[
2^{-t}\sum_{j=0}^{a}\binom tj
 \le \exp(-2b(t)^2/t)=o(1).
\]

With (2.3), the only uncompressed holes lie in the narrow balanced window

\[
\bigl||S\cap Z|-t/2\bigr|<b(t)+O(1).
\tag{2.4}
\]

Consequently, the exact soft gate is not a weighted all-hole condition: it
is `o(W)` aggregate mass in the near-balanced trace window (2.4).

### A still sharper cutoff-free repair functional

The choice of a trace cut is optional.  For every `R subseteq Z`, let

\[
c_R=\#\{(q,S):0\le q\le h,\ S\in H_q(P),\ S\cap Z=R\}.
\]

Partition `2^Z` into complementary pairs

\[
\Pi=\{R,Z\setminus R\}
\]

and put `c_Pi=c_R+c_(Z minus R)`.  Let

\[
L_t=\nu(n-t)+1,
\qquad
\Phi_h(P,Z)=\sum_{\Pi}\min\{c_\Pi,L_t\}.
\tag{2.5}
\]

For one complementary trace pair there are two valid repairs:

* append every lower hole and its upper complement, at cost `2c_Pi`;
* append the two fixed-trace universal blocks, at cost at most `2L_t`.

Choosing the cheaper option independently for every pair proves the exact
cutoff-free bound

\[
\boxed{
\text{shallow repair cost}\le 2\Phi_h(P,Z).}
\tag{2.6}
\]

This dominates every fixed-cut estimate: extreme trace pairs are capped by
the price of two shared blocks, while sparse balanced pairs are paid for
literally.  It is the exact best upper bound obtainable from this particular
choice between whole-trace blocks and literal complementary repairs.

## 3. Combination with the outer reservoir

Fix `epsilon>0`, choose `gamma(m)->infinity` with
`gamma=o(log log m)`, and set

\[
H=\left\lceil(1/2+\varepsilon)\sqrt{n\log n}\right\rceil,
\qquad
h=\left\lceil\sqrt{m(\log\log m+\gamma(m))}\right\rceil.
\tag{3.1}
\]

Take

\[
R=\left\lceil e^{-\gamma(m)/2}W/n\right\rceil
\]

independent reservoir cyclic orders and emit their depth-`H` erosion
blocks.  The exact defect-damping calculation shows that their word length,
their aggregate holes over `h<q<=H`, and the two literal tails are all
`o(W)`.

### Corollary 2 (shallow relaxed central-trace criterion)

It suffices to construct multisets `P_m` of cyclic orders and marked sets
`Z_m`, with `t_m=|Z_m|`, such that

\[
p_m n=W+o(W),\qquad t_m\to\infty,\qquad t_m=o(n),
\tag{3.2}
\]

and for some `a_m<t_m/2` satisfying

\[
2^{-t_m}\sum_{j=0}^{a_m}\binom{t_m}{j}=o(1),
\tag{3.3}
\]

one has

\[
G_{h,a_m}(P_m,Z_m)=o(W).
\tag{3.4}
\]

Then

\[
\nu(2m+1)=W+o(W),
\]

and the trimmed one-bit lift gives the same leading coefficient in even
dimensions.

For an exact middle factor the `q=0` holes vanish.  Taking
`a=floor(alpha t)` reduces (3.4) to the user's sufficient condition
`Delta_h=o(tW)`.  Taking (2.3) is strictly sharper: only shallow holes with
nearly balanced marked trace must have aggregate size `o(W)`.

More generally, conditions (3.3)--(3.4) may be replaced by the single,
strictly weaker cutoff-free condition

\[
\boxed{\Phi_h(P_m,Z_m)=o(W).}
\tag{3.5}
\]

## 4. Remaining content

This theorem does not construct the required `P_m,Z_m`.  It changes the
integral gate to the following precise target:

> Choose `W/n+o(W/n)` cyclic orders and one slowly growing marked set so
> that, through depth `(1+o(1))sqrt(m log log m)`, the truncated
> complementary-trace occupancy `Phi_h` is `o(W)`.

This is weaker than shallow WV, weaker than exact middle ownership, and
strictly stronger than a purely fractional statement.  The same cyclic
family and the same marked set must work at every shallow depth.
