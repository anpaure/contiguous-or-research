# Translation-invariant proportional packet stacks

## Generic internal parallelism, exact product-tail capacity, and the surviving density gate

Date: 2026-07-25

## 0. Verdict and terminology

Fix

\[
n=2m+1,\qquad W=\binom{n}{m},
\]

and, for a fixed constant

\[
\frac1{\sqrt2}<\alpha<\frac{\sqrt3}{2},
\]

put

\[
H=\left\lceil\alpha\sqrt{m\log m}\right\rceil,\qquad
b=\lfloor m^{3/4}\rfloor,\qquad
p=\left\lfloor\frac Wb\right\rfloor,
\]

\[
N_q=\binom{n}{m+q},\qquad
b_q=\left\lfloor\frac{N_q}{p}\right\rfloor
\quad(-H\le q\le H+1).
\tag{0.1}
\]

All theorems below hold for every sufficiently large \(m\) for which
\(n=2m+1\) is prime. This restriction is compatible with the already proved
prime-subsequence/trimmed-lift transfer. No constant-one result is proved
here.

There are two different notions of packet density.

1. **Candidate density.** A packet is internally parallel if its \(n\)
   coordinate translates have no repeated designated target. The proportion
   of labelled proportional atoms which fail this condition is
   \(O(\exp(-c_\alpha m))\).
2. **Packing density.** A family of packets is a parallel class if distinct
   packets also have no common target orbit. If \(M_q=N_q/n\) is the number
   of translation orbits in part \(q\), define

   \[
   \delta(\mathcal M)=
   \min_q\frac{|\mathcal M|b_q}{M_q}.
   \tag{0.2}
   \]

   A positive-density class would have
   \(|\mathcal M|\ge c\,p/n\) for a fixed \(c>0\). The literal constant-one
   reduction needs the stronger estimate

   \[
   |\mathcal M|
   =\left\lfloor\frac pn\right\rfloor
   -o\left(\frac{p}{n\sqrt m}\right).
   \tag{0.3}
   \]

The distinction is decisive:

\[
\boxed{\text{internally parallel candidates have proportion }
1-O(e^{-c_\alpha m}),}
\tag{0.4}
\]

whereas the unconditional cross-packet construction proved here has only

\[
\boxed{
|\mathcal M|=\Omega(W/m^3),\qquad
\delta(\mathcal M)=\Theta(m^{-5/4})=o(1).
}
\tag{0.5}
\]

The second equality means that we may take a subfamily of the certified
size whose coverage fraction has this order; it is not an upper bound on
the true matching number.

Thus translation packetization does not presently supply a positive
packing-density parallel class. It does remove every scalar product-tail
capacity obstruction. The only arithmetic obstruction found is to an exact
all-rank partition; its permitted near-partition residue is \(o(W)\).
Arithmetic-progression packets suffer a separate exact obstruction: their
\(b_q\) same-rank slots collapse to one quotient target with multiplicity
\(b_q\).

No divisibility law obstructing a near-full generic packet matching was
found.

## 1. Proportional atoms and translation packets

Take the nested prefix starts

\[
I_q=\{0,1,\ldots,b_q-1\}.
\tag{1.1}
\]

These are compatible with the homogeneous multiradius profile because the
\(b_q\)'s decrease away from the two middle ranks and
\(b_{-d}=b_{d+1}\). Put

\[
L=m+b+H<n.
\tag{1.2}
\]

An injective word \(x=(x_0,\ldots,x_{L-1})\) has designated targets

\[
A_{i,q}(x)=\{x_i,x_{i+1},\ldots,x_{i+m+q-1}\},
\qquad i\in I_q.
\tag{1.3}
\]

Identify the coordinates with \(\mathbb Z_n\), and let \(T_a\) add
\(a\in\mathbb Z_n\) to every letter. The translation packet of \(x\) is

\[
\mathcal T(x)=\{T_ax:a\in\mathbb Z_n\}.
\tag{1.4}
\]

The action on labelled injective words is free, so every packet has exactly
\(n\) words. Call the packet **internally parallel** when

\[
A_{i,q}(x)+a=A_{j,q}(x)+c
\quad\Longrightarrow\quad (i,a)=(j,c)
\tag{1.5}
\]

for every fixed \(q\) in the band. Targets at different ranks cannot be
equal, so (1.5) is the complete internal-disjointness condition.

Write

\[
r_q=m+q,\qquad
\kappa=\sum_{q=-H}^{H+1}b_q.
\tag{1.6}
\]

Uniformly for the product-tail parameters,

\[
b_0=b_1=b,\qquad
b_{\min}=m^{3/4-\alpha^2+o(1)}\longrightarrow\infty,
\tag{1.7}
\]

and

\[
\kappa=\Theta(b\sqrt m)=\Theta(m^{5/4}).
\tag{1.8}
\]

## 2. Exact internal-collision theorem

### Lemma 2.1 — one positional pair and one translation

Let \(x\) be a uniformly random injective word, fix \(q\), take
\(i\ne j\) in \(I_q\), and put \(d=|i-j|\). For every \(h\ne0\),

\[
\boxed{
\Pr\bigl(A_{j,q}(x)=A_{i,q}(x)+h\bigr)
=\frac{nd}{r_q(n-r_q)N_q}.
}
\tag{2.1}
\]

#### Proof

Extend the word uniformly to a permutation of \(\mathbb Z_n\). Since

\[
d<b<\min(r_q,n-r_q)
\]

for all sufficiently large \(m\), the two positional intervals differ by
exactly \(d\) deleted and \(d\) added positions. Conditional on
\(A_{i,q}=S\), the second target is uniform among the

\[
\binom{r_q}{d}\binom{n-r_q}{d}
\tag{2.2}
\]

sets at Johnson distance \(d\) from \(S\).

Because \(n\) is prime, addition by \(h\ne0\) is one \(n\)-cycle. The
number of \(r_q\)-sets satisfying

\[
|S\setminus(S+h)|=d
\]

is the cyclic-run count

\[
\frac nd
\binom{r_q-1}{d-1}
\binom{n-r_q-1}{d-1}.
\tag{2.3}
\]

Divide (2.3) by \(N_q\) and by (2.2). The identities

\[
\frac{\binom{r-1}{d-1}}{\binom rd}=\frac dr,
\qquad
\frac{\binom{n-r-1}{d-1}}{\binom{n-r}d}
=\frac d{n-r}
\]

give (2.1). \(\square\)

### Theorem 2.2 — almost every proportional packet is internally parallel

Put

\[
D_q=\sum_{\substack{i,j\in I_q\\i\ne j}}|i-j|.
\tag{2.4}
\]

The expected number of relative-translation collision witnesses
\((q,i,j,h)\), with \(i\ne j\) and \(h\ne0\), is exactly

\[
\boxed{
\sum_{q=-H}^{H+1}
\frac{n(n-1)D_q}{r_q(n-r_q)N_q}.
}
\tag{2.5}
\]

For the prefix starts (1.1),

\[
D_q=\frac{b_q(b_q^2-1)}3.
\tag{2.6}
\]

Consequently

\[
\begin{aligned}
\Pr(\mathcal T(x)\text{ is not internally parallel})
&\le \frac{n(n-1)}3
\sum_q\frac{b_q(b_q^2-1)}
{r_q(n-r_q)N_q}\\
&=O\left(\frac{Hb^3}{N_{\min}}\right)\\
&=\frac{m^{11/4+\alpha^2+o(1)}}W
=O(e^{-c_\alpha m}).
\end{aligned}
\tag{2.7}
\]

#### Proof

Sum (2.1) over the \(n-1\) nonzero translations and all ordered start
pairs. This gives (2.5). A collision between two translated atoms has a
unique relative translation \(h\), while a target cannot be fixed by a
nonzero translation when \(n\) is prime. Also, two distinct equal-length
positional intervals in one injective word have different target sets, so
relative translation zero creates no omitted collision. Hence packet
failure implies at least one witness, and Markov's inequality gives the
first line of (2.7).

For a prefix of size \(u\),

\[
2\sum_{0\le i<j<u}(j-i)=\frac{u(u^2-1)}3,
\]

which proves (2.6). In the band,
\(r_q(n-r_q)=\Theta(m^2)\), while

\[
N_{\min}=Wm^{-\alpha^2+o(1)}.
\]

There are \(2H+2\) ranks and \(b_q\le b\), proving the remaining lines.
\(\square\)

The event in Theorem 2.2 depends only on the length-\(L\) prefix. Thus the
same bound holds among labelled proportional atoms, not only among
completed cyclic orders. Generic non-AP packets therefore solve the whole
within-packet synchronization problem at every product-tail rank
simultaneously.

## 3. A stronger target trim and the exact quotient law

The direct theorem proves internal simplicity. A slightly stronger generic
property shows that quotienting also preserves the conditional-overlap
estimate.

Put

\[
J=b+2H+1=o(m).
\tag{3.1}
\]

For an \(r\)-set \(A\), call \(A\) **strongly translation-good** if

\[
|A\setminus(A+h)|>2J
\qquad\text{for every }h\ne0.
\tag{3.2}
\]

### Lemma 3.1 — strong-good targets have exponentially full density

Uniformly at every rank in the band, the proportion of targets which are
not strongly translation-good is \(O(e^{-c_\alpha m})\).

#### Proof

For fixed \(h\ne0\), the exact number with translation boundary \(j\) is

\[
\frac nj\binom{r-1}{j-1}\binom{n-r-1}{j-1}.
\tag{3.3}
\]

Summing (3.3) over \(1\le j\le2J\) gives

\[
\exp(O(J\log m))=\exp(o(m)).
\]

There are fewer than \(n\) choices of \(h\), whereas every central-band
part has \(N_q=\exp(\Theta(m))\). Division by \(N_q\) proves the claim.
\(\square\)

Since one packet has only \(\kappa=m^{5/4+o(1)}\) designated targets, all
targets are strongly good in a
\(1-O(e^{-c_\alpha m})\) fraction of packets. Such a packet is internally
parallel: if two same-rank targets obeyed \(B=A+h\), then

\[
|A\setminus(A+h)|=|A\setminus B|\le J,
\]

contrary to (3.2).

Let

\[
E=(n)_L
\tag{3.4}
\]

be the number of labelled injective words. Quotient words and targets by
the translation group. For prime \(n\), every nonempty proper target has a
free orbit, so part \(q\) has exactly

\[
M_q=\frac{N_q}{n}
\tag{3.5}
\]

quotient vertices, and there are \(E/n\) labelled packet occurrences.
A strongly good packet is a simple quotient hyperedge with \(b_q\)
vertices in part \(q\), hence total edge rank \(\kappa\).

### Proposition 3.2 — exact quotient degree and fractional class

Every quotient target orbit in part \(q\) has incidence degree

\[
\boxed{
\mathfrak d_q=b_q\frac E{N_q}\le\frac Ep.
}
\tag{3.6}
\]

Giving every packet occurrence weight \(p/E\) gives an exact fractional
incidence packing of total weight \(p/n\): the load at a part-\(q\) vertex
is

\[
\mathfrak d_q\frac pE=\frac{pb_q}{N_q}\le1.
\tag{3.7}
\]

After deleting packets which are not strongly good, the same weights give
a simple fractional packing of total at least

\[
\left(1-O(e^{-c_\alpha m})\right)\frac pn.
\tag{3.8}
\]

#### Proof

For one fixed positional slot and one fixed actual target, exactly \(E/N_q\)
words realize that target. Sum over the \(n\) members of one target orbit
and the \(b_q\) slots, and divide by the \(n\) words in a packet. This gives
(3.6). Equations (3.7)–(3.8) follow. \(\square\)

There is also an exact incidence-pair formula. Let \(v=[A]\) be in part
\(q\), let \(w=[B]\) be a distinct quotient vertex in part \(q'\), and
let \(\mathcal S_q\) denote the designated positional intervals of rank
\(q\). Then

\[
\boxed{
\frac{\operatorname{codeg}_{\rm inc}(v,w)}{\mathfrak d_q}
=\frac1{b_q}
\sum_{P\in\mathcal S_q}
\sum_{Q\in\mathcal S_{q'}}
\sum_{t\in\mathbb Z_n}
\frac{
\mathbf1_{\substack{
|A\setminus(B+t)|=|P\setminus Q|\\
|(B+t)\setminus A|=|Q\setminus P|}}}
{\binom{|A|}{|P\setminus Q|}
\binom{n-|A|}{|Q\setminus P|}}.
}
\tag{3.9}
\]

This follows by conditioning on the representative event \(x(P)=A\).
The target in slot \(Q\) is then uniform among sets with the displayed two
set differences; summing over representatives \(B+t\) gives (3.9). On
strongly good vertices these incidence counts are ordinary occurrence
counts. Indeed, if one packet contained a strongly good orbit \(v=[A]\)
in two distinct slots, representatives in those slots would have the form
\(A\) and \(A+t\) with positional boundary at most \(J\), contrary to
(3.2). Thus a strongly good orbit occurs at most once in every packet; for
strongly good \(v,w\), incidence-pair and ordinary occurrence codegree
agree.

### Proposition 3.3 — the \(O(1/m)\) row sum survives quotienting

Let \(e\) be a strongly good packet and \(v\in e\), with \(v\) in part
\(q\). In the full packet-occurrence multihypergraph,

\[
\boxed{
\sum_{w\in e\setminus\{v\}}
\frac{\operatorname{codeg}(v,w)}{\mathfrak d_q}
=O(1/m),
}
\tag{3.10}
\]

uniformly in \(q,e,v\). In addition,

\[
\operatorname{codeg}(v,w)
\le \frac3{m-H}\mathfrak d_q
\tag{3.11}
\]

for distinct vertices in a strongly good test packet.

#### Proof

Take test targets \(A,B\in e\). Every two designated positional intervals
have both set differences at most \(J\). If a nonzero \(t\) contributed to
(3.9), then

\[
|B\setminus(B+t)|
\le |B\setminus A|+|A\setminus(B+t)|
\le2J,
\]

contradicting the strong goodness of \(B\). Thus only \(t=0\) contributes.

For fixed

\[
a=|A\setminus B|,\qquad c=|B\setminus A|,
\]

at most \(a+c+1\) vertices of the test packet have this type relative to
\(A\), and at most \(a+c+1\) candidate positional intervals have the same
type relative to a conditioning slot. Therefore the left side of (3.10)
is at most

\[
\sum_{\substack{0\le a,c\le J\\a+c\ge1}}
\frac{(a+c+1)^2}
{\binom r a\binom{n-r}c}
=O(1/m),
\tag{3.12}
\]

because \(r,n-r\ge m-H\) and \(a,c\le J=o(m)\). For one fixed pair, the
largest term has \(a+c=1\), which also gives the safe bound (3.11).
For completeness, if \(R=m-H\) and \(t\in\{0,1,2\}\), then

\[
\sum_{j=1}^{J}\frac{j^t}{\binom Rj}=O(1/R).
\tag{3.13}
\]

Indeed, the \(j=1\) term is \(O(1/R)\); since \(J=o(R)\), the terms for
\(j\ge2\) are geometrically dominated from \(O(R^{-2})\), even after the
fixed polynomial factor \(j^t\). Expanding \((a+c+1)^2\) and separating
the \(a=0\) or \(c=0\) boundary terms bounds (3.12) by a constant
combination of the one-variable sums (3.13) and their products.
\(\square\)

Thus translation quotienting loses neither the ambient proportional
incidence balance nor the strong local overlap estimate at a strongly good
test edge. Equation (3.10) is normalized by the ambient degree
\(\mathfrak d_q\); no uniform lower bound for degrees after deleting all
bad packets is asserted. These facts still do not round (3.8) to a
positive-density matching when \(\kappa\to\infty\).

## 4. Exact product-tail capacity and divisibility

Write

\[
p=ns+a,\qquad 0\le a<n,\qquad
s=\left\lfloor\frac pn\right\rfloor,
\tag{4.1}
\]

and

\[
N_q=pb_q+\rho_q,\qquad 0\le \rho_q<p.
\tag{4.2}
\]

Since \(n\mid N_q\),

\[
\boxed{
M_q=s b_q+\frac{a b_q+\rho_q}{n}.
}
\tag{4.3}
\]

The last summand is a nonnegative integer. In particular,

\[
s b_q\le M_q
\tag{4.4}
\]

at every product-tail rank. This is the exact cancellation which fails for
equal-size full-wreath packets: the decreasing multiplicities \(b_q\)
track the decreasing capacities \(N_q\).

### Theorem 4.1 — a near-full quotient matching gives constant one

Suppose the simple good-packet quotient hypergraph has a matching of size

\[
s-u,\qquad
u=o\left(\frac{p}{n\sqrt m}\right).
\tag{4.5}
\]

Then its lift consists of

\[
n(s-u)=p-\tau,\qquad
\tau=a+nu=o(p/\sqrt m),
\tag{4.6}
\]

pairwise target-disjoint literal proportional atoms. It therefore gives

\[
\nu(2m+1)\le W+o(W).
\tag{4.7}
\]

#### Proof

A simple quotient edge lifts to its \(n\) internally disjoint translated
atoms. Disjoint quotient edges use disjoint target orbits, so their lifts
are mutually disjoint. At rank \(q\), the exact number of uncovered targets
is

\[
N_q-(p-\tau)b_q=\rho_q+\tau b_q.
\tag{4.8}
\]

The selected literal rows and singleton repairs have total length at most

\[
(p-\tau)(b+2H+1)
+\sum_q(\rho_q+\tau b_q)+T_H,
\tag{4.9}
\]

where the two outer binomial tails have exact nonempty-mask count

\[
T_H=2\sum_{r=0}^{m-H-1}\binom nr-1
=Wm^{1/2-\alpha^2+o(1)}=o(W).
\tag{4.10}
\]

Now

\[
(p-\tau)b\le W,\qquad
pH=O(WH/b)=o(W),
\]

\[
\sum_q\rho_q<(2H+2)p=O(HW/b)=o(W),
\]

and, by (1.8) and (4.6),

\[
\tau\sum_qb_q
=o(p/\sqrt m)\,\Theta(b\sqrt m)=o(W).
\]

Substitution in (4.9) proves (4.7). \(\square\)

For \(u=0\), only \(a<n\) atom slots are lost. The exact leave becomes

\[
U_q=\rho_q+a b_q,
\tag{4.11}
\]

which is divisible by \(n\), as a translation-invariant leave must be, and

\[
\sum_qU_q<(2H+2)p+n\kappa=o(W).
\tag{4.12}
\]

Hence there is no density-scale divisibility loss.

There is nevertheless a genuine obstruction to an exact all-rank parallel
partition. If \(K\) packets covered both ranks \(m\) and \(m-1\) exactly,
then

\[
Knb=W,\qquad
Knb_{-1}=N_{-1}=\frac m{m+2}W.
\]

Eliminating \(K\) gives

\[
(m+2)(b-b_{-1})=2b.
\tag{4.13}
\]

For large \(m\), \(0<2b<m+2\). The left side of (4.13) is divisible by
\(m+2\), so (4.13) is impossible. This exact-partition obstruction is real,
but (4.11)–(4.12) show that its literal cost is \(o(W)\); it does not
obstruct (4.5).

## 5. AP stacks are exactly the wrong packets

Let

\[
x_j=u+jd\pmod n,\qquad d\ne0.
\]

Then at every rank

\[
A_{i+1,q}(x)=A_{i,q}(x)+d.
\tag{5.1}
\]

Thus all \(b_q\) designated slots collapse to one quotient vertex with
multiplicity \(b_q\). In the lifted packet, every target in that orbit is
used \(b_q\) times. Since \(b_0=b>1\), no AP packet is an internally
parallel proportional packet.

This is not repaired by taking more AP rows. The affine group supplies
only polynomially many AP/affine packet shapes, whereas a positive-density
class requires

\[
\Theta(p/n)=\Theta(W/m^{7/4})
\tag{5.2}
\]

packets. Consequently every architecture confined to polynomially many
AP/AGL seed shapes has zero packing density. AP rows can only be negligible
boundary data; generic non-AP packets must carry the leading mass.

## 6. What can be selected unconditionally

Let \(\mathcal R\) be the strongly good packet occurrences. Lemma 3.1 gives

\[
|\mathcal R|
\ge\left(1-O(e^{-c_\alpha m})\right)\frac En.
\tag{6.1}
\]

Every quotient vertex has degree at most

\[
\Delta\le\frac Ep
\tag{6.2}
\]

even before bad packets are deleted. A packet contains \(\kappa\) quotient
vertices, so it intersects at most \(\kappa\Delta\) packet occurrences.
Greedy independent-set selection in the packet intersection graph gives

\[
\begin{aligned}
|\mathcal M|
&\ge\frac{|\mathcal R|}{\kappa\Delta+1}\\
&=(1-o(1))\frac{p}{n\kappa}
=\Omega(W/m^3).
\end{aligned}
\tag{6.3}
\]

This is a genuine family of mutually cross-disjoint, internally parallel
translation packets. By taking a subfamily of the order certified in
(6.3), its coverage fraction at every part is

\[
\frac{\Theta(p/(n\kappa))b_q}{N_q/n}
=\Theta(1/\kappa)
=\Theta(m^{-5/4}).
\tag{6.4}
\]

Thus (6.3) is nontrivial and exponential in \(m\), but its target density
tends to zero. The growing packet rank \(\kappa\) is exactly the factor
separating this greedy construction from positive density.

The \(O(1/m)\) row sum does not remove the first-order conflict count. It
says that, after fixing a vertex \(v\) of a test packet, few competing
packets hit a second test vertex. It does not change the fact that there
are \(\kappa\) first vertices at which a competitor may meet the test
packet.

## 7. Precise no-go for iid residual and two isolated-edge samplers

The preceding gap is not repaired by a quasirandom residual.

Retain each quotient target independently with probability \(z<1\). Every
internally parallel packet is simple and therefore survives with
probability \(z^\kappa\). Since there are at most \(E/n\) packet
occurrences, including invalid ones,

\[
\mathbb E[\text{surviving internally parallel packet occurrences}]
\le\frac En z^\kappa.
\tag{7.1}
\]

Here

\[
\log E=O(m\log m),\qquad
\kappa=\Theta(m^{5/4}).
\]

For every fixed \(z<1\), the right side of (7.1) tends to zero. In fact the
threshold scale at which this iid residual loses all usable internally
parallel packet candidates is

\[
-\log z=\Theta(m^{-1/4}\log m).
\tag{7.2}
\]

Thus a random greedy process whose unused vertices look independent stalls
after only a vanishing covered fraction, long before any fixed positive
density.

The same obstruction appears in the following specific one-shot scheme:
sample from the full ambient packet-occurrence multihypergraph and retain a
strongly good packet only if it is isolated from every other sampled
ambient occurrence. For a strongly good packet \(e\), Proposition 3.3 and
two-term Bonferroni give

\[
|\{f:f\cap e\ne\varnothing\}|
\ge(1-o(1))\kappa\frac Ep.
\tag{7.3}
\]

Indeed, the sum of the \(\kappa\) vertex degrees is
\((1-o(1))\kappa E/p\), while the sum of all pair intersections among those
degree neighborhoods is only \(O(\kappa E/(pm))\). If all ambient packet
occurrences are sampled independently with probability

\[
\rho=c\frac pE
\]

for a fixed \(c>0\), the expected number of sampled strong-good packets
which meet no other sampled ambient packet is at most

\[
\frac En\rho
\exp\left(-(1-o(1))\rho\kappa E/p\right)
\le \frac{cp}{n}\exp(-(1-o(1))c\kappa)=o(1).
\tag{7.4}
\]

There is a slightly weaker but more natural version for sampling only the
pretrimmed strongly good packet family. Call a target **superstrong** if

\[
|A\setminus(A+h)|>4J\qquad(h\ne0).
\tag{7.5}
\]

The run count from Lemma 3.1 shows that the fraction of packets having any
non-superstrong target is \(O(e^{-c_\alpha m})\). Moreover,

\[
\partial_h(A):=|A\setminus(A+h)|
=\frac12|A\triangle(A+h)|
\]

is \(1\)-Lipschitz in symmetric-difference distance:

\[
|\partial_h(A)-\partial_h(B)|
\le |A\triangle B|.
\tag{7.6}
\]

Any two designated targets in one packet have symmetric difference at most
\(2J\). Therefore every packet containing a superstrong target consists
entirely of strongly good targets. It follows that every ambient neighbor
of an all-superstrong test packet lies in the strongly good packet family
\(\mathcal R\).

Now sample only \(\mathcal R\), again with probability \(\rho=cp/E\), and
retain sampled packets which are isolated inside \(\mathcal R\).
For all-superstrong test packets, (7.3)–(7.4) apply unchanged, so their
expected isolated output is \(o(1)\). Packets in
\(\mathcal R\) which are not all-superstrong form only
\(O(e^{-c_\alpha m})E/n\) occurrences, so even the expected number of such
packets sampled before any collision deletion is

\[
O(e^{-c_\alpha m})\frac En\frac{cp}{E}
=o(p/n).
\tag{7.7}
\]

Thus this good-only isolated-edge sampler also has expected output
\(o(p/n)\). By Markov's inequality, its probability of producing any fixed
positive packing density tends to zero.

Equations (7.1)–(7.7) are method-specific no-go theorems. They do not prove
that a structured positive-density or near-full matching is absent. They
prove that such a matching, if it exists, must leave highly correlated
unions of whole packet columns throughout the construction.

## 8. Exact remaining theorem and implication scope

Define the quotient proportional-packet resolution statement

\[
\mathrm{QPPR}_\alpha(m):\qquad
\operatorname{mat}(\overline{\mathcal P}_{m;b,H}^{\rm good})
\ge
\left\lfloor\frac pn\right\rfloor
-o\left(\frac{p}{n\sqrt m}\right).
\tag{8.1}
\]

Theorem 4.1 proves that \(\mathrm{QPPR}_\alpha(m)\) along the odd primes
implies the literal constant-one theorem after the established
prime-subsequence transfer.

What is proved here:

* generic internal packet coherence with exponentially high density;
* exact quotient degrees and an asymptotically full fractional class;
* the ambient \(O(1/m)\) conditional-overlap row sum at every strongly
  good test edge (not uniform post-trim degrees);
* exact proportional capacity at every product-tail rank;
* only an \(o(W)\) divisibility residue for a near-full class;
* an exact AP/affine zero-density obstruction;
* a cross-disjoint construction of \(\Omega(W/m^3)\) packets;
* failure of iid residuals and both explicitly defined isolated-edge
  samplers at every fixed positive density.

What is not proved:

\[
|\mathcal M|\ge c\,p/n
\quad\text{for any fixed }c>0,
\tag{8.2}
\]

let alone the near-full estimate (8.1). No class invariant or divisibility
law obstructing (8.2) was found. The candidate-density theorem (2.7) and
the fractional law (3.7) cannot be quoted as an integral positive-density
parallel class.

The precise surviving gate is a growing-rank, column-correlated quotient
resolution: convert the fractional packet law of total \(p/n\) into an
integral matching while keeping all
\(\kappa=\Theta(m^{5/4})\) slots of each selected packet coherent. The
translation architecture passes the internal and arithmetic tests, but the
global cross-packet test remains open.

## 9. Independent audit of the decisive calculations

1. The probability in (2.1) uses ordered start pairs. Accordingly \(D_q\)
   in (2.6) is twice the unordered distance sum; this accounts for the
   factor \(1/3\), not \(1/6\).
2. Only the relative translation \(h=a-c\) is summed in (2.5). Summing
   separately over \(a,c\) would insert a spurious factor \(n\), because one
   relative witness already certifies the collision of two full packets.
3. A quotient packet edge has \(b_q\), not \(nb_q\), vertices in part
   \(q\). Each quotient vertex represents the complete \(n\)-target orbit
   used by the lifted packet.
4. The quotient edge rank remains \(\kappa=\sum_qb_q\). Quotienting reduces
   both target capacity and atom count by \(n\), but it does not reduce the
   growing-rank matching difficulty.
5. Formula (4.3) is integral because \(n\mid N_q\). It proves capacity
   sufficiency, not existence of a matching.
6. The exact-partition contradiction (4.13) concerns only zero leave. It
   cannot be promoted to an obstruction at the \(o(W)\) leave permitted by
   constant one.
7. The greedy estimate (6.3) is a lower bound on what can be constructed,
   not an upper bound on the true matching number.
8. The iid and isolated-edge calculations in Section 7 rule out only those
   specified sampling models, not a highly correlated integral resolution
   or every possible alteration scheme.

These checks leave (8.1), and already its fixed-positive-density weakening
(8.2), as genuinely unproved integral statements.
