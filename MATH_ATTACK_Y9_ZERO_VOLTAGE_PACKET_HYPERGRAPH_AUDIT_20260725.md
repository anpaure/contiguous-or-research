# Lane Y9 auxiliary audit: the zero-voltage packet hypergraph

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, solver, or
finite search is used.

## 0. Verdict

Let

\[
n=2m+1
\]

be prime, let \(H\le A\sqrt m\), and put

\[
N_q=\binom n{m-q},\qquad M_q=\frac{N_q}{n},
\qquad 0\le q\le H.
\]

There is a natural \((H+1)\)-partite incidence multihypergraph whose
vertices in part \(q\) are translation orbits of \((m-q)\)-sets and whose
edges are translation packets of cyclic orders. A packet which is
translation-rainbow throughout the band is a simple edge with exactly
\(n\) vertices in every part, and at the middle rank it is exactly a
zero-voltage simple \(n\)-cycle in the quotient odd graph.

The following facts are proved below.

1. Before deleting nongeneric packets, every aperiodic vertex in part
   \(q\) has the exact weighted degree

   \[
   d_q=(m-q)!(m+q+1)!=\frac{n!}{N_q}.             \tag{0.1}
   \]

2. After deleting an exponentially negligible set of low-boundary target
   orbits, every pair of distinct vertices satisfies

   \[
   \operatorname{codeg}(v,w)
   \le \frac{12}{m}\min(d_q,d_{q'})               \tag{0.2}
   \]

   for all sufficiently large \(m=m(A)\).

3. The proportion of cyclic orders which are not simultaneously
   translation-rainbow in the whole band is exponentially small. Hence,
   in every part, all but an exponentially small proportion of vertices
   retain degree \((1-o(1))d_q\) in the generic zero-voltage packet
   hypergraph.

Thus the quotient packet system really is locally pseudorandom. This does
**not** prove the required packet selection theorem. There are three exact
reasons.

First, the ordinary uncapacitated matching formulation is impossible. Any
matching has size at most \(M_H/n\), whereas a middle near-factor needs
\((1-o(1))M_0/n\) packets, and

\[
\frac{M_H}{M_0}
=\frac{N_H}{W}
=\exp\left(-\frac{H(H+1)}m+O\left(\frac{H^3}{m^2}\right)\right).
                                                               \tag{0.3}
\]

For \(H=A\sqrt m+O(1)\), this is \(e^{-A^2+o(1)}\), a constant strictly
below one when \(A>0\).

Second, the needed replacement is not merely a bounded-capacity matching.
If \(\ell_q(v)\) is the selected load of a quotient target and
\(c_q=\lfloor W/N_q\rfloor\), then the actual floor energy is

\[
Q_q=n\sum_{v}
 (\ell_q(v)-c_q)(\ell_q(v)-c_q-1).                \tag{0.4}
\]

Consequently an \(O_A(H\operatorname{Cat}_m)\) band-energy estimate forces
all but an \(O_A(1/n)\) proportion of quotient target slots, on average
over the band, to have one of the two exact loads \(c_q,c_q+1\). Local
boundedness of the loads is weaker by a factor of order \(n\).

Third, the packet uniformity is

\[
K=n(H+1)=\Theta_A(m^{3/2}).                       \tag{0.5}
\]

The fixed-uniformity Pippenger--Frankl--Rödl theorem cannot be invoked with
this \(K\). Near-regularity and relative codegree \(o(1)\) do not imply an
almost-perfect matching when uniformity grows; finite projective planes
give a rigorous counterexample to that inference. In the present system
one also has to control the possible multiplicity lost when packet edges
with the same unlabeled shadow set are collapsed.

The proved boundary is therefore:

\[
\boxed{
\text{generic zero-voltage packets have the desired local statistics,
but SCC/GCC requires a new global capacitated floor/ceiling resolution.}}
                                                               \tag{0.6}
\]

The \(q=1\) saturating Johnson cycle is consistent with this conclusion:
at depth one the counting loss is only \(2/(m+2)=o(1)\). It does not
resolve the Gaussian-band capacity loss, nor does it decompose itself into
zero-voltage length-\(n\) packets.

## 1. The quotient packet incidence multihypergraph

Identify the coordinate set with \(\mathbb Z_n\), and let
\(T=\mathbb Z_n\) act by translation. Since \(n\) is prime, this action is
free on every nonempty proper subset. Define

\[
\mathcal O_q=\binom{\mathbb Z_n}{m-q}/T,
\qquad |\mathcal O_q|=M_q.                        \tag{1.1}
\]

Pairing a lower set with its upper complement is implicit: one vertex
\([A]_T\in\mathcal O_q\) records both the lower translation orbit of
\(A\) and the upper translation orbit of \(A^c\).

Let \(\Omega\) be the set of oriented cyclic orders modulo rotation, so

\[
|\Omega|=(n-1)!.                                  \tag{1.2}
\]

For \(C\in\Omega\), write \(I_i^{(r)}(C)\) for its length-\(r\) cyclic
interval at start \(i\), and define the multiplicity

\[
a_{q,v}(C)=
\bigl|\{i\in\mathbb Z_n:[I_i^{(m-q)}(C)]_T=v\}\bigr|.          \tag{1.3}
\]

Translation acts on \(\Omega\). A nontrivial stabilizer occurs precisely
for an arithmetic-progression order; every other orbit has size \(n\).
For a translation class \([C]_T\), use the multiplicities (1.3) as its
incidences. This gives the full packet incidence multihypergraph.

If \(C\) is translation-rainbow at every rank \(m-q\), then every
\(a_{q,v}(C)\) is zero or one and exactly \(n\) of them equal one in every
part. At the middle rank the quotient image is a simple \(n\)-cycle. Its
lift is the closed wreath \(C\), so its total voltage is zero. Thus the
band-rainbow edges are genuine zero-voltage packet edges, not fractional
or rankwise surrogate objects.

## 2. Exact packet degrees

Fix \(r=m-q\) and an actual \(r\)-set \(A\). The number of oriented cyclic
orders modulo rotation in which \(A\) is an interval is

\[
r!(n-r)!=d_q.                                     \tag{2.1}
\]

Indeed, arrange the elements of \(A\) and \(A^c\) internally in the two
consecutive circular blocks. There are \(r!(n-r)!\) resulting orders.

Let \(v=[A]_T\). Its orbit contains \(n\) actual sets. Therefore

\[
\sum_{C\in\Omega}a_{q,v}(C)=n d_q.                \tag{2.2}
\]

If \(v\) is not an AP interval orbit, no AP order contributes to (2.2),
so every contributing order has a free translation orbit. Dividing (2.2)
by \(n\) proves the exact weighted packet degree

\[
\boxed{\deg(v)=d_q.}                              \tag{2.3}
\]

For completeness, an AP interval orbit is met by the two oriented AP
orders of the corresponding unoriented slope, each with multiplicity
\(n\). Removing the stabilized AP packets changes its degree by two.
All AP orbits will be included in the much smaller exceptional set below.

For non-AP target orbits the exact degree ratios are

\[
\boxed{
\frac{d_q}{d_0}=rac{W}{N_q}=:\lambda_q.}        \tag{2.4}
\]

Thus uniform packet weight \(1/d_0\) is an exact fractional quota law on
every non-AP target orbit: it gives load one at the middle part and load
\(\lambda_q\) in part \(q\). On each of the only \(O(n)\) AP target
orbits, deleting the stabilized AP packet changes the weighted degree from
\(d_q\) to \(d_q-2\); equivalently the displayed fractional load has the
explicit negligible defect \(2/d_0\). One may retain the stabilized packet
with translation multiplicity to recover the exact all-target fractional
identity, but that is a fractional multicover, not a selectable full packet.
This is the precise fractional/stationary boundary. It contains no integral
floor/ceiling rounding.

## 3. Exact conditional two-interval count

Let \(|A|=r\), \(|D|=s\), with \(r,s\le m\), and condition on \(A\) being
a cyclic interval of a uniformly random order. The internal linear orders
of \(A\) and \(A^c\) are independent and uniform. Put

\[
p_A(D)=\Pr(D\text{ is a cyclic interval}\mid A\text{ is a cyclic interval}).
                                                               \tag{3.1}
\]

The following formulas are exact.

* If \(D\subsetneq A\), then

  \[
  p_A(D)=\frac{r-s+1}{\binom r{s}}
        =\frac{r-s+1}{\binom r{r-s}}.             \tag{3.2}
  \]

* If \(A\subsetneq D\), then

  \[
  p_A(D)=\frac{s-r+1}{\binom{n-r}{s-r}}.          \tag{3.3}
  \]

* If \(A\cap D=\varnothing\), then

  \[
  p_A(D)=\frac{n-r-s+1}{\binom{n-r}{s}}
        =\frac{n-r-s+1}{\binom{n-r}{n-r-s}}.      \tag{3.4}
  \]

* In the remaining proper-overlap case, if
  \(a=|A\cap D|\) and \(b=|D\setminus A|\), then

  \[
  p_A(D)=
  \frac{2}{\binom r a\binom{n-r}b}.              \tag{3.5}
  \]

For (3.2), \(D\) must be one of the \(r-s+1\) consecutive subblocks of
the random linear order of \(A\). Formula (3.3) is the complementary
statement inside \(A^c\), and (3.4) is the same subblock count in
\(A^c\). In (3.5), \(A\cap D\) must occupy one end of the \(A\)-block and
\(D\setminus A\) the adjacent end of the \(A^c\)-block; the factor two
chooses the side. This proves all four formulas.

Now let \(v=[A]_T\in\mathcal O_q\) and
\(w=[B]_T\in\mathcal O_{q'}\) be distinct packet vertices. Expanding the
two incidence multiplicities and dividing the cyclic orders into free
translation classes gives

\[
\boxed{
\operatorname{codeg}(v,w)
=d_q\sum_{t\in\mathbb Z_n}p_A(B+t).}              \tag{3.6}
\]

This is an exact identity for the full incidence multihypergraph whenever
\(v\) is non-AP. Restricting to band-rainbow packet edges can only decrease
the left side.

## 4. Removing the only large quotient codegrees

For a set \(B\) and a nonzero translation \(t\), put

\[
\partial_t(B)=|B\setminus(B+t)|.                 \tag{4.1}
\]

Call \(B\) \(L\)-aperiodic if \(\partial_t(B)>L\) for every
\(t\ne0\). Take

\[
L=2H+1.                                           \tag{4.2}
\]

### Lemma 4.1 (the exceptional target set is subexponential)

Uniformly for \(0\le q\le H=O_A(\sqrt m)\), the number of
\((m-q)\)-sets which are not \(L\)-aperiodic is

\[
\exp(O_A(\sqrt m\log m))=o(N_q).                  \tag{4.3}
\]

#### Proof

For a fixed nonzero translation \(t\), primality of \(n\) makes it one
\(n\)-cycle. The exact cyclic-run enumeration gives, for \(r=m-q\),

\[
\#\{B:|B|=r,\ \partial_t(B)=j\}
=\frac nj\binom{r-1}{j-1}\binom{n-r-1}{j-1}.     \tag{4.4}
\]

Sum (4.4) over \(t\ne0\) and \(1\le j\le L\). The result is at most
\(n^2L m^{2L}\), which is
\(\exp(O_A(\sqrt m\log m))\). On the other hand every central
\(N_q\) is \(\exp(\Theta(m))\). This proves (4.3). \(\square\)

### Lemma 4.2 (quotient pair-codegree bound)

Suppose \(A,B\) are \(L\)-aperiodic, their sizes lie in
\([m-H,m]\), and their translation orbits define distinct packet
vertices. If \(H\le m/3\), then, for all sufficiently large \(m\),

\[
\sum_{t\in\mathbb Z_n}p_A(B+t)\le\frac{12}{m}.    \tag{4.5}
\]

#### Proof

There is at most one translate \(B+t\) contained in \(A\). Indeed, if
two such translates existed and \(d=|A|-|B|\), then

\[
|B\cup(B+u)|\le |B|+d
\]

for a nonzero \(u\), hence \(\partial_u(B)\le d\le H<L\), a
contradiction. The same intersection argument shows that at most one
translate of \(B\) can contain \(A\). Finally, at most one translate of
\(B\) can be disjoint from \(A\), because two would lie in \(A^c\), whose
excess size over \(B\) is

\[
n-|A|-|B|=1+q+q'\le2H+1=L.                       \tag{4.6}
\]

Two such translates would again give a nonzero translation boundary at
most \(L\).

According to the relative sizes, at most one of the first two containment
types is possible, and the disjoint type may also occur. By
(3.2)--(3.4), each of these at most two exceptional terms is at most

\[
\frac{2}{m-H}.                                    \tag{4.7}
\]

Every remaining translate is in the proper-overlap case. Since both
intersection pieces are nonempty and proper, (3.5) gives

\[
p_A(B+t)\le\frac{2}{|A|(n-|A|)}
\le\frac{2}{(m-H)(m+1)}.                          \tag{4.8}
\]

There are at most \(n\) such terms. Therefore

\[
\sum_t p_A(B+t)
\le\frac4{m-H}+\frac{2n}{(m-H)(m+1)}
\le\frac{12}{m},                                  \tag{4.9}
\]

where the last inequality uses \(H\le m/3\). \(\square\)

Combining (3.6) and Lemma 4.2, and then reversing the roles of the two
vertices, proves

\[
\boxed{
\operatorname{codeg}(v,w)
\le\frac{12}{m}\min(d_q,d_{q'}).}                \tag{4.10}
\]

This quotient estimate is not the unquotiented estimate with notation
changed: equation (3.6) has a sum over all relative translations. The
aperiodicity lemma is what prevents that sum from creating a constant
relative codegree.

## 5. Deleting nongeneric packets preserves almost all degrees

Let \(\Omega_{\rm bad}\) be the cyclic orders which fail translation
rainbowness at one of the ranks \(m,m-1,\ldots,m-H\). The exact
translation-collision first moment gives

\[
\varepsilon_m:=\frac{|\Omega_{\rm bad}|}{|\Omega|}
\le n^2(n-1)\sum_{q=0}^H\frac1{N_q}
\le\frac{n^2(n-1)(H+1)}{N_H}
=e^{-\Theta_A(m)}.                                \tag{5.1}
\]

Let \(\mathscr G_{m,H}\) be the packet hypergraph consisting only of the
band-rainbow translation classes. Every such class has size \(n\), and
every edge is simple with exactly \(n\) vertices in each part. Thus

\[
\sum_{v\in\mathcal O_q}\deg_{\mathscr G}(v)
=n|E(\mathscr G)|
=|\Omega\setminus\Omega_{\rm bad}|.              \tag{5.2}
\]

Since

\[
M_qd_q=\frac{N_q}{n}\frac{n!}{N_q}=(n-1)!=|\Omega|,             \tag{5.3}
\]

the average degree in part \(q\) is exactly
\((1-\varepsilon_m)d_q\). Markov's inequality applied to the degree
deficits shows that, for every \(\tau>0\), all but at most
\((\varepsilon_m/\tau+o(1))M_q\) vertices have degree at least
\((1-\tau)d_q\); the \(o(1)\) includes the subexponential exceptional
orbits from Lemma 4.1. Taking \(\tau=\sqrt{\varepsilon_m}\) proves the
claimed almost-everywhere near-regularity. Equation (4.10) remains valid
after the edge deletion.

This is the strongest conclusion justified by the counts. Distinct cyclic
orders may in principle collapse to the same unlabeled quotient shadow
edge. The calculations above are for the natural incidence
**multihypergraph**. Pair codegree bounds the multiplicity of any one
collapsed edge by \(O(d_q/m)\), but it does not prove that collapsing all
parallel packet descriptions preserves degree \((1-o(1))d_q\). A positive
simple-hypergraph nibble would need this additional multiplicity audit or
would need a theorem formulated directly for the incidence
multihypergraph.

## 6. The uncapacitated matching has a constant Gaussian deficit

A matching in \(\mathscr G_{m,H}\) uses \(n\) different vertices in every
part for each selected packet. Therefore

\[
|\mathcal M|\le\frac1n\min_{0\le q\le H}M_q
=\frac{M_H}{n}.                                   \tag{6.1}
\]

To cover all but \(o(M_0)\) middle quotient vertices one needs

\[
|\mathcal M|=(1-o(1))\frac{M_0}{n}.               \tag{6.2}
\]

But

\[
\frac{M_H}{M_0}
=\frac{\binom n{m-H}}{\binom nm}
=\prod_{j=0}^{H-1}\frac{m-j}{m+j+2}.              \tag{6.3}
\]

For \(H=O(\sqrt m)\), Taylor expansion with a uniform remainder gives

\[
\log\frac{M_H}{M_0}
=-\frac{H(H+1)}m+O\left(\frac{H^3}{m^2}+\frac H{m^2}\right).   \tag{6.4}
\]

Equations (6.1)--(6.4) prove (0.3). Hence an ordinary matching across the
Gaussian band cannot be the desired theorem, regardless of how strong a
matching theorem one imports.

At \(q=1\), by contrast,

\[
\frac{M_1}{M_0}=\frac{m}{m+2}=1-\frac2{m+2}.      \tag{6.5}
\]

This explains why the complete lower-rainbow Johnson cycle can saturate
the relaxed depth-one count up to \(o(W)\). The phenomenon does not extend
to \(q=A\sqrt m\) without target multiplicities.

## 7. Exact quota strength forced by floor energy

Suppose a set of band-rainbow translation packets is selected. For
\(v\in\mathcal O_q\), let \(\ell_q(v)\) be the number of selected packet
edges containing \(v\). Lifting a packet gives all \(n\) coordinate
translations of its wreath. Since the packet is internally rainbow, every
actual set in the orbit \(v\) then has load exactly \(\ell_q(v)\).
Therefore

\[
Q_q
=n\sum_{v\in\mathcal O_q}
f_q(\ell_q(v)),
\qquad
f_q(x)=(x-c_q)(x-c_q-1).                           \tag{7.1}
\]

For integral \(x\), \(f_q(x)\ge0\), it vanishes precisely for
\(x\in\{c_q,c_q+1\}\), and otherwise \(f_q(x)\ge2\). In the fixed
Gaussian window, \(1\le c_q\le C_A\) for a constant depending only on
\(A\). Hence

\[
\sum_{q=1}^H\frac{Q_q}{c_q}=O_A(HB),
\qquad B=\frac Wn,
                                                               \tag{7.2}
\]

implies

\[
\sum_{q=1}^H\sum_{v\in\mathcal O_q}f_q(\ell_q(v))
=O_A\left(\frac{HB}{n}\right).                   \tag{7.3}
\]

Since \(|\mathcal O_q|=M_q=\Theta_A(B)\), (7.3) says that the proportion
of non-floor/ceiling quotient slots, averaged over the band, is
\(O_A(1/n)\). Thus a theorem which only produces
\(\ell_q(v)\le C_A\) allows \(\Theta_A(HB)\) bad quotient slots and, after
the factor \(n\) in (7.1), only proves \(Q=O_A(HW)\). It misses the desired
scale by a factor of order \(n\).

The exact remaining combinatorial statement is consequently a
capacitated, lower-quota packet resolution:

> select \((1-o(1))M_0/n\) zero-voltage packet edges, with exact middle
> ownership after an \(o(M_0)\) residue, so that the load at all but
> \(O_A(HB/n)\) quotient shadow slots belongs to
> \(\{c_q,c_q+1\}\).

Neither (2.4) nor the pair-codegree estimate rounds this fractional quota
law.

## 8. Why the standard nibble citation is invalid here

The generic packet edge has uniformity

\[
K=n(H+1)=\Theta_A(m^{3/2}).                       \tag{8.1}
\]

The classical Pippenger--Frankl--Rödl almost-perfect matching theorem is a
fixed-\(K\) theorem: for each fixed \(K\) and error tolerance it supplies
a codegree threshold. One cannot substitute \(K=K(m)\) into its qualitative
statement.

Moreover, no theorem based only on

\[
\deg(v)=(1+o(1))D,qquad \Delta_2=o(D),qquad D\to\infty             \tag{8.2}
\]

can hold for growing \(K\). Let \(s\) run through powers of two and take
the point-line hypergraph of the projective plane over \(\mathbb F_s\).
It is \((s+1)\)-uniform and \((s+1)\)-regular, any two points have
codegree one, and hence

\[
\frac{\Delta_2}{D}=\frac1{s+1}\longrightarrow0.                 \tag{8.3}
\]

Yet every two lines intersect, so its matching number is one and it covers
a vanishing proportion of the vertices. If arbitrarily large degree is
desired in the multihypergraph category, repeat every line the same number
of times; the relative codegree remains \(1/(s+1)\) and the matching number
is unchanged.

This example does not prove that the specific packet hypergraph lacks a
large quota matching. It proves rigorously that Lemmas 4.2 and 5.1 are not
sufficient hypotheses for one. A positive proof must exploit an additional
global expansion, absorber, alternating-cycle, or explicit cyclic
resolution property of the packet system, uniformly at
\(K=\Theta_A(m^{3/2})\).

## 9. Final proved/conditional boundary

The exact positive content is:

* full translation packets are automatically integral and zero voltage;
* after removal of exponentially few structured targets and packets, their
  quotient incidence multihypergraph is almost regular with relative pair
  codegree \(O_A(1/m)\);
* away from the \(O(n)\) explicitly identified AP orbits, uniform packet
  weighting gives the exact fractional means \(\lambda_q=W/N_q\); the AP
  defect is exactly \(2/d_0\), or disappears if stabilized packets are
  retained with translation multiplicity.

The exact negative content is:

* an ordinary all-depth packet matching loses the constant fraction
  \(1-e^{-A^2}+o(1)\) at the middle layer;
* bounded capacities do not imply the required floor energy;
* fixed-uniformity nibble theorems do not apply, and growing-uniformity
  degree/codegree data alone are logically insufficient;
* simple-edge multiplicity after quotient collapse remains unaudited.

No SCC, GCC, MWB, literal contiguous-OR theorem, or constant-one theorem is
claimed. The new sharply isolated gate is the capacitated zero-voltage
floor/ceiling resolution stated after (7.3).
