# Cyclic star packets: exact incidence, fractional abundance, and the growing-uniformity gate

**Date:** 2026-08-06  
**Method:** exact double counting and cyclic-interval enumeration  
**Status:** unconditional.  The common-core star-packet hypergraph has an
explicit fractional matching with far more than the theta-deficit capacity,
and its pair codegrees are (O(1/n)) of a vertex degree in the central PBBS
range.  Elementary greedy packing is nevertheless smaller than the required
constant-density packing by a polynomial factor.  Standard fixed-uniformity
matching theorems, and the usual ABKV growing-uniformity criterion, do not
justify the missing rounding.

## 1. Packet hypergraph

Fix an (n)-set, a bottom rank (s), a depth (d), and put

\[
                         N=n-s+1.
\]

Let (d+1\le L\le N).  An oriented cyclic (L)-packet consists of

* a core (Q\in{[n]\choose s-1});
* a private set (R\in{[n]\setminus Q\choose L}); and
* an oriented cyclic order of (R), modulo rotation.

Its target edge is

\[
 E(Q,R,\omega)=
 \left\{Q\cup I_{i,j}(\omega):i\in\mathbb Z/L\mathbb Z,
                                  1\le j\le d\right\},                 \tag{1.1}
\]

where (I_{i,j}) is the cyclic interval of (j) private labels ending at
(i).  It has exactly (Ld) vertices, (L) in each rank
(s,s+1,\ldots,s+d-1).

The number of packet edges is

\[
 \boxed{
 P_L={n\choose s-1}{N\choose L}(L-1)! .}                              \tag{1.2}
\]

Reversals are distinct in this convention.  Quotienting by reversal divides
all degrees below by the same factor two and changes none of the conclusions.

## 2. Exact vertex degrees

Let (V_j={[n]\choose s+j-1}), (1\le j\le d).  Every target in (V_j)
has the same packet degree

\[
 \boxed{
 D_{j,L}={s+j-1\choose j}{N-j\choose L-j}j!(L-j)!
        ={(s+j-1)!\over(s-1)!}{(N-j)!\over(N-L)!}.}                    \tag{2.1}
\]

Indeed, for a fixed target (S\in V_j), choose its core
(Q\subset S) in ({s+j-1\choose j}) ways, choose the other (L-j)
private labels outside (S), and contract the prescribed (j)-set to one
cyclic block.  The number of cyclic orders containing that block is
(j!(L-j)!).

The incidence identity is

\[
                         P_LL=|V_j|D_{j,L}.                             \tag{2.2}
\]

Successive degrees satisfy the exact ratio

\[
                         {D_{j+1,L}\over D_{j,L}}
                         ={s+j\over N-j}.                              \tag{2.3}
\]

In particular, throughout the top full PBBS slab

\[
 n=2m+1,\qquad s=m-2d,\qquad 1\le j\le d,
\]

the degrees decrease with (j), so (D_{1,L}) is the maximum degree.

## 3. Exact pair codegrees

Take distinct targets

\[
 S\in V_j,\qquad T\in V_k.
\]

Write

\[
 |S\cap T|=s-1+a,\qquad u=j+k-a.
\]

If (a<0) or (u>L), their codegree is zero.  Otherwise

\[
 \boxed{
 D_{j,k,a;L}^{(2)}=
 {s-1+a\choose s-1}{N-u\choose L-u}\,
 \kappa_L(j,k,a),}                                                     \tag{3.1}
\]

where (kappa_L(j,k,a)) is the number of oriented cyclic orders of a
fixed (L)-set in which fixed (j)- and (k)-subsets with intersection
size (a) are both cyclic intervals.

For (u<L), this number is exactly

\[
\kappa_L(j,k,a)=
\begin{cases}
 j!k!(L-j-k+1)!,&a=0,\\[2mm]
 2(j-a)!(k-a)!a!(L-u)!,&0<a<\min(j,k),\\[2mm]
 j!(k-j+1)!(L-k)!,&a=j<k,\\[2mm]
 k!(j-k+1)!(L-j)!,&a=k<j.
\end{cases}                                                            \tag{3.2}
\]

When (u=L), complements turn the two-interval condition into two
disjoint interval blocks, and

\[
 \boxed{
 \kappa_L(j,k,a)=(L-j)!(L-k)!(a+1)! .}                                \tag{3.3}
\]

### Proof

Any common packet core is an ((s-1))-subset of (S\cap T), giving the
first factor in (3.1).  Once the core is fixed, the two private subsets have
union size (u), and the remaining private labels can be chosen in the
second factor's number of ways.

For (3.2), contract the two disjoint blocks when (a=0).  In the proper
overlap case the circle, outside the union, has the unique block pattern

\[
 (S\setminus T),(S\cap T),(T\setminus S)
\]

or its reverse.  In the containment cases, contract the smaller interval
inside the larger one.  These contractions give the four displayed
factorials.  If (u=L), both sets are intervals exactly when their two
nonempty complements are disjoint intervals; contracting those complements
gives (3.3).  \(\square\)

Two consecutive nested targets exhibit the largest first-order ratios:

\[
 {D_{j,j+1,j;L}^{(2)}\over D_{j,L}}={2\over N-j},\qquad
 {D_{j,j-1,j-1;L}^{(2)}\over D_{j,L}}={2\over s+j-1}.                  \tag{3.4}
\]

The formulas above also show that, uniformly in the central range
(s,N-d=\Theta(n)),

\[
 \max_{S\ne T}{\deg(S,T)\over\deg(S)}=O(1/n).                         \tag{3.5}
\]

All noncontainment cases pay two independent denominator factors; all
containments separated by (h>1) pay respectively

\[
 {(h+1)!\over(N-j)_{\underline h}}
 \quad\hbox{or}\quad
 {(h+1)!\over(s+k)^{\overline h}},                                    \tag{3.6}
\]

and are smaller than the one-step cases for the PBBS parameters once (n)
is large.  Equation (3.3) also pays both a core-side and an outside-side
factor and is smaller still.

## 4. Exact fractional packing

Assume (D_{1,L}\ge D_{j,L}) for (1\le j\le d), as in the top full
slab.  Give every packet weight (1/D_{1,L}).  Every target has total
incident weight at most one.  Hence this is a fractional matching of size

\[
 {P_L\over D_{1,L}}={|V_1|\over L}.                                   \tag{4.1}
\]

It fractionally serializes exactly

\[
                         L{P_L\over D_{1,L}}=|V_1|={n\choose s}         \tag{4.2}
\]

full pieces.  Thus the star-packet problem has no scalar or fractional
capacity obstruction.

For the top full slab, (s=m-2d), the local central limit estimate gives

\[
 {{n\choose s}\over W}\longrightarrow e^{-\pi}.                      \tag{4.3}
\]

The theta reset deficit is only

\[
 \eta W+o(W),\qquad
 \eta=2\sigma-1=4\sum_{q\ge1}e^{-4\pi q^2}
       =0.0000139\ldots .                                               \tag{4.4}
\]

Since (eta/e^{-\pi}\approx3.23\cdot10^{-4}), the fractional packet
capacity exceeds the required deficit by a factor greater than three
thousand asymptotically.

## 5. What elementary integral packing proves

A packet conflicts with at most

\[
                         L\sum_{j=1}^d D_{j,L}                          \tag{5.1}
\]

packets, counting itself and harmless repetitions.  Greedy selection in
the packet conflict graph therefore gives a target-disjoint family of at
least

\[
 \boxed{
 {P_L\over L\sum_jD_{j,L}}
 \ge { {n\choose s}\over L^2d}}                                      \tag{5.2}
\]

packets, and hence at least

\[
                         {{n\choose s}\over Ld}                        \tag{5.3}
\]

serialized full pieces.

This bound rigorously compares the two natural packet lengths:

* (L=d+1=\Theta(\sqrt n)) gives (Omega(W/n)) pieces;
* (L=N=\Theta(n)) gives (Omega(W/n^{3/2})) pieces.

Thus elementary greedy packing favours short packets, but neither estimate
reaches the required (eta W) constant-density bank.

## 6. Why the familiar matching black boxes do not close the gap

The packet hypergraph has growing uniformity

\[
                         K=Ld.                                         \tag{6.1}
\]

For (L=d+1), (K=\Theta(n)); for (L=N),
(K=\Theta(n^{3/2})).  Meanwhile (3.4) shows that the normalized maximum
pair codegree is genuinely of order (1/n), not exponentially small in
(K).

Therefore fixed-uniformity Pippenger--Spencer/Frankl--Rödl theorems cannot
be quoted with (K=K(n)).  The usual ABKV growing-uniformity hypothesis

\[
                         e^{2K}\Delta_2\log D=o(D)                     \tag{6.2}
\]

also fails, since (Delta_2/D=\Theta(1/n)) on the nested one-step pairs
in (3.4).  The left side of (6.2), normalized by (D), is at least of
order (e^{2Ld}\log D/n).

The exact fractional matching (4.1), large margin (4.4), and small
normalized codegrees (3.5) make a specialized switching or nibble theorem
plausible.  They do not constitute such a theorem at growing uniformity.

## 7. Exact remaining statement

The local theta repair would follow from the following genuinely integral
claim:

> In the top full slab (s=m-2d), the cyclic star-packet hypergraph has a
> target-disjoint matching serializing at least
> ((2\sigma-1+o(1))W) bottom targets.

Fractionally, this claim has a margin exceeding (3000).  Unconditionally,
the present greedy argument serializes only (o(W)) targets.  Closing that
rounding gap is a specialized growing-uniformity star-factor problem.

Even that theorem would close only the theta full-piece reset row.  A full
(B(k)+O(1)) construction must still place the selected packets in the
varying PBBS owner envelopes, connect them in one owner-compatible Euler
order, and preserve the short-piece/global compiler interface.

