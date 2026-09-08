# The standard SCD in the rotor graph

## 0. Outcome

For the standard Greene--Kleitman/de Bruijn--Tengbergen--Kruyswijk symmetric
chain decomposition of \(B_{2m}\), the induced radius-\(d\) rotor graph is
empty for every \(d\ge1\).  Thus its minimum path cover has
\[
p_d=c_d=N_d-N_{d+1},
\qquad N_d=\binom{2m}{m-d}.
\tag{0.1}
\]
This remains true after every coordinate relabeling.

Consequently the standard SCD fails the proposed condition by a factor
\(\Theta(\sqrt m)\).  For \(H=\lceil A\sqrt m\rceil\), even after omitting
the clipped top class,
\[
\boxed{
\frac1{W\sqrt m}
\sum_{d=1}^{H-1}(2d+2)p_d
\longrightarrow
4\int_0^A x^2e^{-x^2}\,dx
=\sqrt\pi\,\operatorname{erf}(A)-2Ae^{-A^2}>0.
}
\tag{0.2}
\]
Over every positive native radius, the exact toll is
\[
\boxed{
\sum_{d=1}^m(2d+2)p_d=4^m-W+2N_1.
}
\tag{0.3}
\]

This gives a quantitative obstruction to the standard SCD, not to the
existence of a different SCD.  A recursive rotor packet supplies the
opposite local behavior: all its same-radius chains form one rotor cycle.
Moreover, arbitrary mixed radius choices inside one such packet remain
mask-disjoint.  Hence a global decomposition into homogeneous recursive
packets would give the desired \(o(W)\) start toll.  Constructing those
packets as one full SCD is the unresolved common-base completion problem.

## 1. Rotor signatures

An oriented radius-\(d\) saturated chain is written
\[
\omega=(L;z_1,\ldots,z_{2d};R),
\qquad |L|=|R|=m-d.
\tag{1.1}
\]
Its masks are
\[
L, L+z_1, \ldots, L+z_1+\cdots+z_{2d}.
\]
For \(d\ge1\), a directed rotor successor has signature
\[
\omega'=
(L-x+y;\ x,z_1,\ldots,z_{2d-1};\ R-y+z_{2d}),
\qquad x\in L,quad y\in R.
\tag{1.2}
\]

In particular, a rotor successor must have first singleton coordinate
\(x\), lying strictly before the old first persistent singleton in the BTK
signature derived below.

## 2. The BTK parenthesis signature

Fix the coordinate order \(1<2<\cdots<2m\).  Encode a BTK chain by its
ballot word in letters \(U,D\), using the usual stack matching: every
\(D\) is paired with the most recent unmatched \(U\).  For a word ending
at height \(2d\), let

* \(L\) be the relevant matched \(D\)-positions;
* \(R\) be their matched \(U\)-positions; and
* \(z_1<\cdots<z_{2d}\) be the persistent unmatched \(U\)-positions.

These data give exactly the oriented chain state (1.1).  Moving along the
BTK chain changes the persistent letters in their increasing positional
order.

### Theorem 2.1 -- no positive-radius BTK rotor edge

No two distinct radius-\(d\) chains of the BTK SCD are joined by a directed
rotor edge when \(d\ge1\).

### Proof

Assume that a rotor successor exists.  It changes only two letters of the
ballot word,
\[
q_x:D\longmapsto U,
\qquad
q_y:U\longmapsto D,
\tag{2.1}
\]
and (1.2) requires the new persistent unmatched sequence to be
\[
x,z_1,\ldots,z_{2d-1}.
\tag{2.2}
\]
Thus necessarily \(x<z_1\).

Suppose first that \(x<y\).  In the old word, the \(D\) at \(x\) is
matched, so the stack immediately before \(x\) is nonempty.  After changing
that letter to \(U\), if the new \(U\) at \(x\) survived as the first
persistent unmatched letter, then every old stack item below it would also
survive.  That would create a persistent unmatched \(U\) strictly before
\(x\), contradicting (2.2).

Suppose instead that \(y<x\).  After position \(x\), the old and new words
have identical letters and identical height.  The new \(U\) at \(x\)
occupies the stack level formerly occupied by an old pre-\(x\) item.  Since
\(z_1>x\), every such old item is eventually popped.  The identical future
height descent therefore also pops the new item at \(x\), again
contradicting (2.2).

Both possible orders of \(x,y\) are impossible. \(\square\)

A coordinate permutation is an automorphism of every rotor graph and sends
the BTK SCD to its relabelled copy.  Hence the empty-induced-graph conclusion
holds throughout the full coordinate orbit of the standard SCD.

## 3. Exact and asymptotic start tolls

Every full SCD of \(B_{2m}\) has
\[
c_d=N_d-N_{d+1}
=N_d\frac{2d+1}{m+d+1}
\tag{3.1}
\]
native radius-\(d\) chains.  Theorem 2.1 gives \(p_d=c_d\) for the BTK SCD
at every \(d\ge1\).

For fixed \(A\), uniformly for \(d\le A\sqrt m+O(1)\),
\[
\frac{N_d}{W}
=\exp\!\left(-\frac{d^2}{m}+O_A(m^{-1/2})\right).
\tag{3.2}
\]
Set \(d=x\sqrt m\).  Equations (3.1)--(3.2) give
\[
(2d+2)c_d
=(4x^2e^{-x^2}+o_A(1))W.
\]
The mesh size in \(x\) is \(m^{-1/2}\).  Summation proves (0.2).  The
clipped class \(d=H\) is not used, so no assertion about how longer BTK
chains interact after clipping is needed.

For the complete native-radius sum, summation by parts gives
\[
\begin{aligned}
\sum_{d=1}^m(2d+2)(N_d-N_{d+1})
&=4N_1+2\sum_{d=2}^mN_d\\
&=2\sum_{d=1}^mN_d+2N_1.
\end{aligned}
\]
By symmetry of the Boolean ranks,
\[
\sum_{d=1}^mN_d=\frac{4^m-W}{2},
\]
which proves (0.3).

## 4. What any successful SCD must look like

Fix a Gaussian annulus
\[
a\sqrt m\le d\le b\sqrt m,
\qquad0<a<b<\infty.
\]
Throughout it,
\[
c_d=\Theta_{a,b}(W/\sqrt m).
\tag{4.1}
\]
If a spanning rotor path forest has average path length
\[
\ell_d^{\rm av}=c_d/p_d,
\]
then its weighted contribution at radius \(d\) is
\[
(2d+2)p_d
=\Theta_{a,b}\!\left(\frac{W}{\ell_d^{\rm av}}\right).
\tag{4.2}
\]
There are \(\Theta(\sqrt m)\) radii in the annulus.  Hence an \(o(W)\)
total toll forces
\[
\sum_{d\text{ in annulus}}rac1{\ell_d^{\rm av}}=o(1).
\tag{4.3}
\]
In particular, at a typical Gaussian radius the successful SCD must join
almost all chains into rotor runs of length \(\omega(\sqrt m)\).  BTK has
\(\ell_d^{\rm av}=1\) everywhere.

This also shows why modifying only \(o(W)\) chain states around BTK is not a
plausible repair: the successful SCD needs a positive-density reorganization
through every Gaussian annulus, not a sparse collection of local splices.

### 4.1 The standard two-coordinate recursion is also obstructed

The failure is not confined to one fixed parenthesis convention.  Start
with an arbitrary SCD of \(B_{2m}\), tensor each parent chain with a new
two-coordinate square, and in every parent box choose either of the two
standard SCD phases.  In the resulting SCD of \(B_{2m+2}\), every native
radius-\(d\) outer child arising from a parent radius-\((d-1)\) chain has
indegree zero in the induced rotor graph.

Indeed, the two new coordinates occupy the last two singleton positions
\(2d-1,2d\) of the outer child.  A rotor predecessor would have to place
them in source singleton positions \(2d-2,2d-1\).  The exhaustive four
standard child signatures place the new coordinates respectively

* in positions \(2d-1,2d\);
* one in the lower block and one in position \(2d\);
* one in each residual block; or
* both in the lower block.

None has the required predecessor signature.  Hence
\[
p_d\ge c_{d-1}^{(m)}.
\tag{4.4}
\]
Summing over a fixed Gaussian window again gives an
\(\Omega_A(W_m\sqrt m)\) weighted toll, independently of every local phase
choice.  Thus a successful SCD cannot arise from the usual \(B_2\)-product
recursion with only sparse repairs; it needs nonstandard cross-parent
splicing on a dense set of chains.

## 5. A positive local theorem from recursive packets

Let a recursive orientation-cycle packet have middle owners
\[
Z_0,Z_1,\ldots,Z_{2\ell-1}
\]
and, for every \(0\le q\le d\le\ell/2\), define
\[
L_q(i)=\bigcap_{j=0}^q Z_{i+j},
\qquad
U_q(i)=\bigcup_{j=0}^q Z_{i-j}.
\tag{5.1}
\]
The radius-\(d\) chain at start \(i\) is
\[
\mathcal C_{i,d}:
L_d(i)\subset\cdots\subset L_1(i)subset Z_i
\subset U_1(i)\subset\cdots\subset U_d(i).
\tag{5.2}
\]
For each fixed \(d\), the \(2\ell\) states
\(\mathcal C_{i,d}\) form one directed rotor cycle and are pairwise
mask-disjoint.

The following mixed-radius strengthening is immediate but useful.

### Proposition 5.1 -- arbitrary radius labels remain disjoint

Choose an arbitrary radius
\[
d_i\in\{0,1,\ldots,\lfloor\ell/2\rfloor\}
\]
for every start \(i\).  Then the \(2\ell\) chains
\[
\{\mathcal C_{i,d_i}:0\le i<2\ell\}
\]
are pairwise mask-disjoint.

### Proof

At rank \(m-q\), chain \(i\) contributes a mask exactly when
\(d_i\ge q\), and that mask is \(L_q(i)\).  The full radius-\(q\) packet
shows that the masks \(L_q(i)\), over all starts \(i\), are distinct.
Likewise, at rank \(m+q\), the possible masks are the pairwise distinct
\(U_q(i)\).  Middle owners \(Z_i\) are distinct as well.  Different ranks
cannot collide. \(\square\)

If all labels in one packet equal \(d\), cutting one rotor edge gives a
path cover of its \(2\ell\) chains with one component.  Suppose, therefore,
that the middle layer could be partitioned into recursive packets of length
\(2\ell=\Theta(m)\), and that packets could be assigned homogeneous radii
so that exactly \(c_d\) owners receive radius \(d\), with only
\(O(\ell)\) residual owners at each radius.  Proposition 5.1 would make the
result a mask-disjoint chain family, provided shadows from different packets
were also disjoint.  Its start toll would be
\[
O\!\left(
\frac1\ell\sum_{d\le H}(2d+2)c_d
+\ell H^2
\right).
\tag{5.3}
\]
For \(\ell=\Theta(m)\) and \(H=A\sqrt m\), the first term is
\(O_A(W/\sqrt m)\) and the second is polynomial in \(m\), hence \(o(W)\).

Thus the rotor adjacency itself has ample local capacity.  The missing
assertion is global:

> choose mask-disjoint recursive packets and their homogeneous radius labels
> so that, at every rank, the packet shadows partition that Boolean rank and
> the residual chains complete to one full SCD.

This is a common-base, all-rank integral completion theorem.  It is not
supplied by the standard SCD or by the exact fractional rotor/SCD
multicover.

## 6. Calibrated status

The answer for the standard Greene--Kleitman/BTK decomposition is decisive:
its positive-radius rotor path cover has one component per chain and weighted
toll \(\Theta(W\sqrt m)\), so it is maximally unsuitable.

The general existence question remains open.  Recursive packets prove that
long runs of the required \(\Theta(m)\) scale are locally compatible with
mask-disjoint symmetric chains.  What is not proved is their simultaneous
global resolution into a single SCD.  A successful construction must be
dense, arc-correlated, and non-BTK; neither coordinate relabeling nor sparse
surgery can supply it.
