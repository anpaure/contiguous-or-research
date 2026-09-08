# GMM Corollary 2: provenance, triple-union fibres, and the exact lexical-transfer barrier

Date: 2026-07-26

Method: pure mathematics and local primary-source audit only.  No finite
search, computation, solver, or web input is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad
 \mathcal L=\binom{[n]}{m-1},\quad
 \mathcal X=\binom{[n]}m,\quad
 \mathcal U=\binom{[n]}{m+1},
\]

\[
 W=|\mathcal X|=|\mathcal U|,
 \qquad N=|\mathcal L|=\frac m{m+2}W,
 \qquad d=W-N=\frac{2W}{m+2}.
\tag{0.1}
\]

The linear upper-collision theorem for the Gregor--Jäger--Mütze--Sawada--
Wille (GJM) lower lexical forest does **not** currently apply to the
two-level saturating cycle cited in Gregor--Mička--Mütze (GMM), Corollary 2.
The two objects come from different theorems and have different edge sets.

More precisely:

1. In the literal two-level case, the proof of GMM Corollary 2 invokes
   Mütze--Su, *Bipartite Kneser graphs are Hamiltonian*, Theorem 9.  It does
   not invoke the GJM four-level lexical factor.
2. The GJM first-global-minimum injection proves

   \[
   \delta_{\rm lex}\ge B_m:=\binom{2m-1}{m-2}
   =\left(\frac14+O(m^{-1})\right)W
   \tag{0.2}
   \]

   for one particular lexical map.  It is not a construction-free theorem
   about every lower-rainbow Johnson cycle.
3. There is an exact transfer law.  If a lower-saturating cycle changes the
   lexical edge at only \(s\) lower colours, then its upper collision excess
   is at least \(B_m-s\).  Consequently any cycle with upper collision
   excess \(o(W)\) must reroute at least

   \[
                         \left(\frac14-o(1)\right)W
   \tag{0.3}
   \]

   lower colours away from the GJM lexical forest.
4. For the actual two-level cycle, the unconditional local estimate is only

   \[
   \max_U k_U\le m,
   \qquad
   |\{U:k_U>0\}|\ge \left\lceil\frac Nm\right\rceil,
   \tag{0.4}
   \]

   where \(k_U\) is the upper-colour multiplicity.  An exact owner-leave
   identity below gives a further conditional collision certificate, but
   it can force only \(O(W/m)\), never a linear fraction, by itself.

Thus no linear obstruction to the Mütze--Su/GMM triple-union support is
proved here.  What is proved is that citing the GJM \(W/4\) theorem against
that cycle without an explicit overlap theorem is invalid.  Conversely,
sparse component fusion of the GJM lexical forest cannot produce a
near-injective saturating cycle.

## 1. The two meanings of “two levels” must be separated

The local primary source `tmp/central/gmlc2.tex` contains two different
parameters which are easy to conflate.

* In the **central levels problem**, the parameter \(\ell=2\) means the
  middle \(2\ell=4\) Boolean levels.  The source attributes that earlier
  case to GJM.
* In **Corollary 2**, the parameter \(\ell=2\) means literally two
  consecutive Boolean levels.  In lines 268--270 of the local source, its
  proof explicitly cites `MR3759914`, Theorem 9.  The bibliography identifies
  `MR3759914` as Mütze--Su, *Bipartite Kneser graphs are Hamiltonian*.

The same GMM paper later constructs central-level cycle factors using
Greene--Kleitman chains and lexical matchings.  That does not change the
provenance of the two-level Corollary, which was delegated to Mütze--Su.
In particular, “the GMM saturating cycle” denotes an existential output,
not a canonically specified GJM lexical edge set.

## 2. Exact triple-union normal form

Write a two-level saturating cycle between ranks \(m-1\) and \(m\) as

\[
 R_0,X_0,R_1,X_1,\ldots,R_{N-1},X_{N-1},R_0,
\tag{2.1}
\]

where the \(R_i\)'s are all members of \(\mathcal L\), the \(X_i\)'s are
distinct members of \(\mathcal X\), and

\[
                         R_i\subset X_i\supset R_{i+1}.
\tag{2.2}
\]

Then

\[
 X_i=R_i\cup R_{i+1},
 \qquad
 X_{i-1}\cap X_i=R_i.
\tag{2.3}
\]

Hence the projected owner sequence \(C=X_0X_1\cdots X_{N-1}X_0\) is one
simple Johnson cycle, and every lower colour occurs exactly once.  Its
upper colour at the edge of lower colour \(R_i\) is

\[
 \psi_C(R_i)=U_i
 :=X_{i-1}\cup X_i
 =R_{i-1}\cup R_i\cup R_{i+1}.
\tag{2.4}
\]

For \(U\in\mathcal U\), put

\[
 k_U=|\{i:U_i=U\}|,
 \qquad
 c_+(C)=N-|\{U:k_U>0\}|=\sum_U(k_U-1)_+.
\tag{2.5}
\]

The number of missing upper targets is exactly \(d+c_+(C)\).  Therefore
the desired opposite-colour estimate is precisely \(c_+(C)=o(W)\).

### Theorem 2.1 (fixed-upper fibre is a linear forest)

For every \(U\in\mathcal U\), form a graph \(H_U\) on vertex set \(U\) by
putting \(ab\in E(H_U)\) exactly when the cycle contains the Johnson edge

\[
 \bigl(U\setminus\{a\}\bigr)
 \bigl(U\setminus\{b\}\bigr).
\tag{2.6}
\]

Then \(H_U\) is a linear forest and

\[
                         k_U=|E(H_U)|\le m.
\tag{2.7}
\]

Consequently (0.4) holds.

#### Proof

The \(m\)-facets of \(U\) are naturally indexed by their missing
coordinates \(a\in U\).  Two such facets are Johnson adjacent, and their
union is \(U\).  Thus \(H_U\) is exactly the subgraph of the abstract cycle
\(C\) induced by those owner vertices which are facets of \(U\).

There are only \(m+1\) facets of \(U\), whereas \(N>m+1\) for \(m\ge2\).
They are therefore a proper subset of the vertices of the one cycle \(C\).
The subgraph of a cycle induced by a proper vertex subset is a disjoint
union of paths and isolated vertices.  Hence \(H_U\) is a linear forest on
at most \(m+1\) vertices and has at most \(m\) edges.  Summing
\(\sum_U k_U=N\) gives the support bound. \(\square\)

This is the full construction-free gain from the elementary fixed-fibre
argument.  It is far weaker than near-injectivity.

## 3. What the GJM first-minimum theorem actually proves

Let \(F_{\rm lex}\) be the GJM lower lexical contraction in dimension
\(2m+1\).  It has one edge \(f_R\) for every \(R\in\mathcal L\).  If the
binary word \(x\) represents \(R\), its upper colour
\(\psi_{\rm lex}(x)\) is obtained by changing the last two down-steps in
the specified lexical row scan to up-steps.

For every word \(y\) of length \(2m-1\) and weight \(m-2\), split

\[
                         y=A0B
\tag{3.1}
\]

at the zero which first attains the global minimum.  The two distinct lower
words

\[
                         x=A010B,
 \qquad                  x'=A001B
\tag{3.2}
\]

satisfy

\[
                         \psi_{\rm lex}(x)
                         =A111B
                         =\psi_{\rm lex}(x').
\tag{3.3}
\]

The domain pairs in (3.2) are disjoint as \(y\) varies.  Hence the lexical
duplicate excess satisfies (0.2).  This theorem uses the displayed lexical
rule at its decisive step.  The triple-union map (2.4) of an arbitrary
saturating cycle has no such rule.

There is also an immediate structural non-identification.  The GJM object
\(F_{\rm lex}\) is a spanning linear forest on all \(W\) middle owners,
with \(N=W-d\) edges and \(d\) components.  The projection \(C\) in
(2.1) is one cycle on only \(N\) middle owners, omitting \(d\) owners.
Thus their edge sets are not equal.  This topological distinction alone
does not imply that their symmetric difference is linear: an
\(O(d)=O(W/m)\)-size rerouting is not excluded by component counts.

## 4. Exact stability of the lexical obstruction

### Theorem 4.1 (map-edit stability)

Let \(\phi,\psi:\mathcal L\to\mathcal U\) be arbitrary maps, and put

\[
 s=|\{R:\phi(R)\ne\psi(R)\}|.
\tag{4.1}
\]

Then

\[
 \bigl||\operatorname{im}\phi|-|\operatorname{im}\psi|\bigr|\le s,
\tag{4.2}
\]

and therefore their duplicate excesses obey

\[
 \left|
 \bigl(N-|\operatorname{im}\phi|\bigr)
 -\bigl(N-|\operatorname{im}\psi|\bigr)
 \right|\le s.
\tag{4.3}
\]

#### Proof

Change the values of the map one input at a time.  Replacing one value can
remove at most one old image point and create at most one new image point;
the image cardinality changes by at most one.  Iterating over the \(s\)
changed inputs proves (4.2), and (4.3) is equivalent. \(\square\)

For a fixed lower colour \(R\), the pair \((R,U)\) determines the unique
Johnson edge between the two intermediate sets of the interval
\([R,U]\).  Thus

\[
 \psi_C(R)=\psi_{\rm lex}(R)
 \quad\Longleftrightarrow\quad
 e_R(C)=f_R(F_{\rm lex}).
\tag{4.4}
\]

Applying Theorem 4.1 and (0.2) gives the exact transfer inequality

\[
 \boxed{
 c_+(C)\ge
 \binom{2m-1}{m-2}
 -|\{R:e_R(C)\ne f_R(F_{\rm lex})\}|.}
\tag{4.5}
\]

### Corollary 4.2 (linear rerouting is necessary)

If \(c_+(C)=o(W)\), then

\[
 |\{R:e_R(C)\ne f_R(F_{\rm lex})\}|
 \ge \binom{2m-1}{m-2}-o(W)
 =\left(\frac14-o(1)\right)W.
\tag{4.6}
\]

Conversely, the GJM collision theorem would yield a linear obstruction for
the cited two-level cycle if one first proved that it agrees with the
lexical forest on \(N-o(W)\) lower colours.  Neither GMM Corollary 2 nor the
local source material supplies that overlap theorem.

## 5. Exact owner-leave moment test for the actual cycle

Let

\[
 \mathcal E=\mathcal X\setminus V(C),
 \qquad |\mathcal E|=d,
 \qquad e_a=|\{X\in\mathcal E:a\in X\}|.
\tag{5.1}
\]

Define

\[
 \kappa
 :=2\binom{2m}{m-1}
   -\binom{2m}{m-2}
   -\binom{2m}{m}
 =\frac{d(m-1)}{2m+1}.
\tag{5.2}
\]

The binomial expression shows in particular that \(\kappa\) is an integer.

### Theorem 5.1 (upper-discrepancy/owner-leave identity)

For every coordinate \(a\in[n]\),

\[
 \boxed{
 \sum_{\substack{U\in\mathcal U\\a\in U}}(k_U-1)
 =\kappa-2e_a.}
\tag{5.3}
\]

Consequently

\[
 \boxed{
 c_+(C)\ge
 \frac1{m+1}
 \sum_{a\in[n]}(\kappa-2e_a)_+.}
\tag{5.4}
\]

#### Proof

Fix \(a\).  Count incidences between cycle edges and their two middle
endpoints which contain \(a\).  Every used owner has cycle degree two, so
the count is

\[
 2\left(\binom{2m}{m-1}-e_a\right).
\tag{5.5}
\]

For one Johnson edge with lower colour \(R\) and upper colour \(U\), the
number of its two endpoints containing \(a\) equals
\(\mathbf1_{a\in R}+\mathbf1_{a\in U}\).  The lower colours exhaust
\(\mathcal L\) exactly once.  Hence the same count is

\[
 \binom{2m}{m-2}
 +\sum_{U\ni a}k_U.
\tag{5.6}
\]

Equating (5.5) and (5.6), then subtracting the full upper-layer point
degree \(\binom{2m}{m}\), proves (5.3).  Elementary binomial ratios give
the second expression in (5.2).

Write

\[
 p_U=(k_U-1)_+,
 \qquad h_U=\mathbf1_{\{k_U=0\}}.
\]

Then \(k_U-1=p_U-h_U\), and

\[
 \sum_U p_U=c_+(C).
\tag{5.7}
\]

If the left side of (5.3) is positive, it is at most
\(\sum_{U\ni a}p_U\).  Summing over all positive coordinates counts every
unit of \(p_U\) at most \(m+1\) times.  Thus

\[
 \sum_a(\kappa-2e_a)_+
 \le (m+1)\sum_U p_U=(m+1)c_+(C),
\]

which is (5.4). \(\square\)

The moment certificate is exact but intrinsically sublinear.  Indeed

\[
 \frac1{m+1}\sum_a(\kappa-2e_a)_+
 \le\frac{(2m+1)\kappa}{m+1}
 =\frac{d(m-1)}{m+1}=O(W/m).
\tag{5.8}
\]

Thus point degrees can expose a Catalan-scale defect in a specified
Mütze--Su owner leave, but cannot reproduce the GJM linear collision
theorem.  A linear obstruction requires construction-specific higher-order
information, such as the first-minimum collision injection itself.

## 6. Exact proved boundary

The following statements are unconditional.

1. The two-level saturating cycle used by GMM Corollary 2 is sourced from
   Mütze--Su Theorem 9; the GJM four-level lexical factor is a distinct
   construction.
2. Every such cycle has the triple-union normal form (2.4), fixed-fibre cap
   (2.7), and owner-leave identity (5.3).
3. The GJM lexical map has at least \(B_m=(1/4-o(1))W\) duplicate excess.
4. This lexical excess survives every \(s\)-label rerouting with loss at
   most \(s\), giving (4.5).
5. Hence no sparse fusion or \(o(W)\)-edge edit of the GJM lexical forest
   can yield a near-injective two-level saturating cycle.

The following statement remains unproved:

\[
 \boxed{
 c_+(C)
 =N-\left|
 \{R_{i-1}\cup R_i\cup R_{i+1}:i\in\mathbb Z_N\}
 \right|
 =o(W)
 }
\tag{6.1}
\]

for some Mütze--Su/GMM two-level saturating cycle, or a linear lower bound
for the particular cycle produced by an explicitly audited implementation
of Mütze--Su's construction.

To transfer the full \((1/4-o(1))W\) negative bound, it is sufficient to
prove the overlap estimate

\[
 |\{R:e_R(C)\ne f_R(F_{\rm lex})\}|=o(W).
\tag{6.2}
\]

More generally, (4.5) is the exact stability threshold supplied by this
argument: an \(\varepsilon W\) collision lower bound follows whenever the
number of changed labels is at most \(B_m-\varepsilon W\).  The minimum
positive escape from the lexical obstruction is necessarily a linear
rerouting, quantified by (4.6).  Without either a sufficiently strong
explicit overlap theorem or a direct analysis
of the Mütze--Su successor rule, the sign of (6.1) is genuinely open.

## 7. Adversarial audit

* The word “lexical” is not a transferable hypothesis.  Two constructions
  may both use Greene--Kleitman ideas while choosing different two-neighbour
  pairs at a lower vertex.  The first-minimum proof needs equality of the
  actual map values, not similarity of terminology.
* Acyclic forest versus one cycle proves nonidentity, but not a linear
  symmetric-difference bound.  It must not be used as a substitute for
  (6.2).
* Formula (4.5) is one-sided in the correct direction: retained lexical
  collisions survive arbitrary new connector edges.  It does not say that
  every linear rerouting removes them.
* Formula (5.4) depends on the owner leave of the same cycle.  Corollary 2
  gives its cardinality \(d\), but no coordinate profile.  Substituting a
  leave from another construction would repeat the same provenance error.
* Neither (0.4) nor (5.4) proves near-injectivity.  The only theorem-level
  conclusion about the cited cycle's upper support from the available
  source is the weak fixed-fibre bound and the conditional moment test.

After these qualifications, all displayed identities and transfer
inequalities above are proved.
