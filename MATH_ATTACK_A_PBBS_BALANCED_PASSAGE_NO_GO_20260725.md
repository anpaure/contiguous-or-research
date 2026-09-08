# Balanced PBBS passages do not admit a local \(O(g/d)\) charge

Date: 2026-07-25

No computation, finite search, or web search is used.

## 0. Verdict

Let \(d\) denote the rank of the equality-particle PBBS and put
\(p=2d+1\).  Perfect orbitwise balance of its omitted-particle word does
not imply that predecessor passages of gap \(g\) occupy an
\(O(g/d)\)-fraction of an orbit.  This fails in the actual PBBS, already
at \(g=7\): a defect-one component has such passages at one third of its
time origins although every particle is omitted exactly three times.

The failure persists with the exact Pascal fibre weights and with
edge-disjoint outer return intervals.  At outer rank \(R=4d-1\), one
three-core reduced orbit has total capacity \(3P\), while its gap-seven
passage supports an edge-disjoint parent packing of size

\[
 (1-o(1)){P\over18},
 \qquad P=\binom{4d}{2d}.
\]

Thus every universal local or orbitwise estimate of the form

\[
 \operatorname{pack}(\mathcal O,g)
 \le C{g\over d}\sum_{E\in\mathcal O}P_R(E)
\]

is false.

This is not a counterexample to \(\mathrm{RP}_A\).  More generally, all
outer roots whose first-pruned core has sufficiently small linear peak
defect have exponentially negligible total Pascal mass.  Hence the exact
surviving gate is a global passage inequality in the high-core-defect
sector; rank, balance, and local fibre capacity alone cannot prove it.

## 1. The balanced defect-one component

For \(a,c\ge0\), \(b\ge1\), and \(a+b+c=d-1\), put

\[
 E(a,b,c)=(10)^a1(10)^b0(10)^c.
\]

The exact PBBS root map and voltage are

\[
 \phi E(a,b,c)=E(b-1,c+1,a),
 \qquad \delta(E(a,b,c))=2(a+1).
\tag{1.1}
\]

Take

\[
 E_*=E(d-2,1,0)=(10)^{d-2}1100.
\]

The three successive roots and voltages are

\[
 \begin{array}{c|c}
 E(d-2,1,0)&p-3\\
 E(0,1,d-2)&2\\
 E(0,d-1,0)&2.
 \end{array}
\tag{1.2}
\]

Thus \(\phi^3E_*=E_*\), while the three-step physical voltage is
\(p+1\equiv1\pmod p\).  The physical PBBS component therefore has period
\(3p\).  Normalizing its first omitted particle to zero, (1.2) gives

\[
 \boxed{
 \kappa_{3j}=j,
 \qquad \kappa_{3j+1}=j-3,
 \qquad \kappa_{3j+2}=j-1
 }
 \quad(j\in\mathbb Z_p).
\tag{1.3}
\]

Each particle label occurs once in each residue class modulo three, hence
exactly three times in the component.  The omitted-particle word is
perfectly balanced.

### Theorem 1.1 (constant-density predecessor passages)

For every \(j\in\mathbb Z_p\), the origin \(t=3j\) is a predecessor
passage of gap seven: particle \(j\) is reselected first at time \(t+5\),
and its predecessor \(j-1\) is selected once before the endpoint and is
selected at time \(t+7\).

#### Proof

Subtracting \(j\) from the seven entries of (1.3) beginning at \(3j\)
gives

\[
 0,-3,-1,1,-2,0,2,-1.
\]

Thus the first later zero is at offset five, the endpoint at offset seven
is the predecessor, and that predecessor has occurred exactly once before
the endpoint, at offset two.  These are precisely the predecessor-passage
conditions, with prescribed seam slot \(z=(1-1)/2=0\).  \(\square\)

In particular the passage origins have density at least \(1/3\), whereas
\(7/d\to0\).  This already disproves every passage-frequency conclusion
based only on PBBS orbit balance.

## 2. Exact Pascal-weighted and edge-disjoint failure

Lift the reduced core to outer rank \(R\).  Since
\(\operatorname{pk}(E_*)=d-1\), its full inverse-pruning fibre and its
gap-seven, empty-seam hyperplane have sizes

\[
 P_R(E_*)=\binom{R+1}{2d},
 \qquad
 K_R(E_*,0)=\binom R{2d-1},
\tag{2.1}
\]

and hence

\[
 {K_R(E_*,0)\over P_R(E_*)}={2d\over R+1}.
\tag{2.2}
\]

Choose \(R=4d-1\).  Then

\[
 P:=P_R(E_*)=\binom{4d}{2d},
 \qquad K_R(E_*,0)={P\over2}.
\tag{2.3}
\]

The step-two reduced orbit has the same three roots as (1.2), in a
different order, and all three have the same fibre capacity \(P\).
Consequently its total reduced-edge capacity is \(3P\).

A gap-seven outer return interval contains five consecutive quotient
transition edges.  On every long parent quotient cycle, greedy selection
retains at least one ninth of any collection of such starts.  For
\(H=O(\sqrt R)\), the number of starts on quotient cycles of length at
most \(H+1\) is

\[
 \exp(O(H\log R))=\exp(o(R))=o(P).
\]

Therefore the exact gap-seven hyperplane supplies an edge-disjoint outer
packing of size

\[
 \boxed{|\mathcal P|\ge(1-o(1)){K_R(E_*,0)\over9}
       =(1-o(1)){P\over18}.}
\tag{2.4}
\]

It follows both that

\[
 {|\mathcal P|\over P}\ge {1\over18}-o(1)
\]

and that

\[
 {|\mathcal P|\over3P}\ge {1\over54}-o(1).
\]

Since \(g/d=7/d\to0\), (2.4) disproves an \(O(g/d)\) charge to either
the starting fibre or the entire reduced orbit.  Notice that this is an
edge-disjoint failure; overlapping passage starts are not responsible.

## 3. The bad local orbit is globally negligible

The preceding obstruction has low core complexity.  The following lemma
shows that this is not an accidental feature of the displayed example.

For a reduced core \(E\in\mathcal D_d\), write

\[
 e(E)=d-\operatorname{pk}(E)
\]

for its own peak defect.  Its rank-\(R\) Pascal capacity is

\[
 P_R(E)=\binom{R+e(E)}{2d}.
\tag{3.1}
\]

### Lemma 3.1 (small core-defect capacity is exponentially negligible)

There are absolute constants \(c,\eta>0\) such that

\[
 1+\sum_{\substack{1\le d<R,\ E\in\mathcal D_d\\e(E)\le cR}}
 P_R(E)
 \le e^{-\eta R}{\operatorname{Cat}_R\over R}
\tag{3.2}
\]

for all sufficiently large \(R\).

#### Proof

Fix \(e=e(E)\).  The number of rank-\(d\) cores with this defect is the
Narayana number

\[
 {1\over d}\binom de\binom d{e+1}.
\tag{3.3}
\]

The initial \(1\) in (3.2) is the empty-core fibre and is harmless.

Nonzero inverse capacity requires

\[
 R-d-\operatorname{pk}(E)=R-2d+e\ge0,
\]

so \(2d\le R+e\), and always

\[
 P_R(E)\le2^{R+e}.
\tag{3.4}
\]

Choose a sufficiently small fixed \(c>0\).  If \(d\le5cR\), the number
of possible cores is at most \(4^d\), so the total exponential rate in
(3.3)--(3.4) is at most

\[
 (1+11c)\log2.
\tag{3.5}
\]

If \(d>5cR\), then, for large \(R\), both \(e/d\) and \((e+1)/d\) are at
most \(1/4\).  With

\[
 h(x)=-x\log x-(1-x)\log(1-x),
\]

the entropy bound and \(2d\le(1+c)R\) give exponential rate at most

\[
 (1+c)\bigl(h(1/4)+\log2\bigr).
\tag{3.6}
\]

Now

\[
 h(1/4)=\log4-{3\over4}\log3<\log2,
\]

because \(3^3>2^4\).  Hence \(c\) can be fixed so small that both (3.5)
and (3.6) are strictly below \(\log4\).  Polynomially many choices of
\((d,e)\) do not change the exponential rate, whereas

\[
 {\operatorname{Cat}_R\over R}
 =\exp(R\log4-o(R)).
\]

This proves (3.2) for some \(\eta>0\).  \(\square\)

The defect-one orbit in Sections 1--2 lies in the negligible sector of
Lemma 3.1.  Thus it closes the proposed *local* weighted charge but does
not numerically challenge \(\mathrm{RP}_A\).

## 4. Exact remaining statement

Neither of the following can prove the required residence estimate:

1. perfect balance of the omitted-particle word on each PBBS component;
2. a local or orbitwise \(O(g/d)\) charge using the reduced rank \(d\),
   even after exact Pascal weighting and edge-disjoint selection.

After Lemma 3.1, one may discard at \(o(\operatorname{Cat}_R/R)\) cost
all first-pruned cores with \(e(E)\le cR\).  The smallest surviving version
of this lane is therefore:

> prove an aggregate capacitated passage-packing inequality of cost
> \(o(\operatorname{Cat}_R/R)\) for reduced cores with
> \(e(E)>cR\), using correlations between different PBBS core orbits or
> their lifted slot-vector traces.

The displayed counterexample does not address a bound whose denominator
is the core peak defect \(e(E)\), rather than the reduced rank \(d\).
Such a bound would still need a global trace-capacity argument strong
enough to reach little-oh at the \(1/R\) quotient scale.

## 5. Adversarial audit

* The period computation is not an appeal to homomesy: it follows directly
  from the three exact PBBS voltages in (1.2), and (1.3) verifies balance
  label by label.
* The passage at time seven includes the necessary earlier reselection at
  time five and has odd predecessor count one; it is not merely an endpoint
  congruence.
* The factor \(1/9\) in (2.4) is the closed conflict-neighbourhood bound
  for five-edge directed intervals.  Short parent cycles are removed before
  applying it.
* The three fibre capacities are equal because both rank and peak number
  are invariant around this reduced orbit.
* Lemma 3.1 counts all inverse lifts through the exact Narayana multiplicity
  and Pascal capacity; it is not an unweighted statement about reduced
  cores.
* The result disproves only local/orbitwise \(O(g/d)\) passage charges.  Its
  total mass is exponentially sub-Catalan, so no failure of \(\mathrm{RP}_A\)
  or of the constant-one conjecture is claimed.
