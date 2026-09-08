# Affine second-moment pair rigidity: exact gain and the unit-shell obstruction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let

\[
 \chi_1(S)=\sum_{x\in S}h(x),
 \qquad
 \chi_2(S)=\sum_{x\in S}h(x)^2
\]

for the same balanced affine coordinate hash
\(h:[2m]\to\mathbb F_p\).  No second independent hash, and hence no
second hash-entropy cost, is introduced.

The pair \((\chi_1,\chi_2)\) rigidifies every affine target pair for
which at least one symmetric-difference block has size at least two:
the affine slope \(\alpha\) is determined up to sign.  Equivalently, all
higher-defect pair shells have only \(O(1)\) possible affine slopes.

The statement is false on the three unit shells

\[
 (a,b)=(1,0),(0,1),(1,1).
\]

There the relevant difference blocks are singletons.  Their second
moments are already determined by their first moments, and
\(\Theta(p)\) different slopes remain possible.  These are precisely the
vertical cover/cocover shells and the same-rank Johnson shell which lead
the raw bow-tie calculation.  Thus the quadratic moment cleans up the
factorially decaying tail, but does not by itself settle the dominant
cross-slice four-walk.

---

## 1. Exact moment trace

Write

\[
 h(a_i)=A+\alpha i,
 \qquad
 h(b_i)=B+\alpha i,
 \qquad
 \delta=B-A.
\]

At lower depth \(d\), one consecutive transition replaces
\(a_{t+d}\) by \(b_t\).  Therefore

\[
 \boxed{
 \Delta\chi_1=\delta-\alpha d,}
 \tag{1.1}
\]

and

\[
 \boxed{
 \Delta\chi_2
 = (\delta-\alpha d)
   (A+B+\alpha d+2\alpha t).}
 \tag{1.2}
\]

At upper depth \(d\), the analogous formulas have
\(\delta+\alpha d\).  Thus \(\chi_1\) is affine in phase and
\(\chi_2\) is quadratic in phase.  Since
\(\delta\pm\alpha d\ne0\) in the protected band, none of these traces
degenerates.

---

## 2. Two moments recover an arithmetic block

Let

\[
 R=\{x,x+\alpha,\ldots,x+(j-1)\alpha\}
 \subseteq\mathbb F_p,
 \qquad 2\le j<p-1.
\]

Put

\[
 s_1(R)=\sum_{r\in R}r,
 \qquad
 s_2(R)=\sum_{r\in R}r^2.
\]

### Lemma 2.1 (AP moment rigidity)

The values \(j,s_1(R),s_2(R)\) determine \(\alpha^2\), and hence
\(\alpha\) up to sign.  Once the sign is chosen, they determine \(x\).

#### Proof

Translation cancels from the centered second moment:

\[
 \begin{aligned}
 j s_2(R)-s_1(R)^2
 &=\alpha^2\left(
 j\sum_{i=0}^{j-1}i^2-left(\sum_{i=0}^{j-1}i\right)^2
 \right)\\
 &=\boxed{
 \alpha^2\frac{j^2(j^2-1)}{12}.}
 \end{aligned}
 \tag{2.1}
\]

The coefficient is nonzero in \(\mathbb F_p\) for the trimmed block
range \(2\le j\le p-2Q-1<p-1\), for all sufficiently large odd primes
\(p\).  Thus \(\alpha^2\) is fixed.  For either square root \(\alpha\),

\[
 x=j^{-1}s_1(R)-\alpha(j-1)/2.
\]

This proves the lemma.  \(\square\)

---

## 3. Rigidity of physical target pairs

Take two physical targets \(S,T\) occurring in affine rows of the same
trimmed slice.  Because the physical sets themselves are known, so are
the four quantities

\[
 \chi_1(S\setminus T),\quad
 \chi_2(S\setminus T),\quad
 \chi_1(T\setminus S),\quad
 \chi_2(T\setminus S).
 \tag{3.1}
\]

In a return-free affine row, each nonempty symmetric-difference block is
a consecutive arithmetic block of the corresponding departure or arrival
string, with common difference \(\alpha\).  Hence Lemma 2.1 gives:

### Proposition 3.1 (off-unit-shell rigidity)

Fix the signed ranks and the ordered physical target pair \((S,T)\).  If

\[
 \max\{|S\setminus T|,|T\setminus S|\}\ge2,
 \tag{3.2}
\]

then at most two affine slopes \(\alpha\) can realize \((S,T)\), the two
being negatives of one another.  For each slope, the relevant affine
block starts are fixed.  Thus the parameters \((A,B,t)\) are fixed up to
the common phase-translation redundancy of the same row trace.

In particular:

* two same-rank targets at phase distance \(j\ge2\) have only \(O(1)\)
  affine slope classes;
* two nested same-phase targets with rank gap at least two have only
  \(O(1)\) affine slope classes;
* every mixed pair shell except \((1,0),(0,1),(1,1)\) is rigid in this
  sense.

The remaining multiplicity for fixed affine parameters comes from the
choice of physical representatives inside the hash classes.  That
multiplicity is exactly the membership-atom codegree already present in
the raw catalogue; it is not an additional parameter collision.

---

## 4. The exact unit-shell failure

For a singleton \(R=\{r\}\),

\[
 s_2(R)=s_1(R)^2.
\]

Therefore \(\chi_2\) contains no information beyond \(\chi_1\).
Given a physical cover pair \(S\subset T\), \(|T\setminus S|=1\), the
hash fixes the one added residue but leaves \(\alpha\in\mathbb F_p^\times\)
free after compensating the affine start.  The same holds for a cocover
pair and for a same-rank Johnson pair, where both symmetric-difference
blocks are singletons.

Consequently the proposed blanket assertion

\[
 \text{``one ordered physical target pair lies in only }O(1)
 \text{ affine slices''}
\]

is false.  It fails by a factor \(\Theta(p)\) on exactly

\[
 (a,b)=(1,0),(0,1),(1,1).
 \tag{4.1}
\]

No finite list of subset-sum power moments can recover a slope from one
physical singleton: all powers are functions of the already known
residue \(h(r)\).

These unit shells are not negligible.  The cover/cocover shell is the
leading \(m^{-1}\) squared-row contribution, while the same-rank Johnson
shell leads the \(m^{-2}\) block.  The raw triangle theorem handles their
uniform average, but arbitrary outer slice weights can still concentrate
on their affine slope classes.

---

## 5. What the quadratic moment actually removes

The new moment has a precise, limited use:

1. all higher-defect shells in the cross-slice pair table are rigid up to
   reversal;
2. their already factorially decaying raw census therefore survives an
   affine parameter decomposition without an additional polynomial
   multiplicity loss;
3. the only parameter-dispersal theorem still needed is for the three
   unit shells (4.1), together with the common scalar compensator drift.

Thus the outer-slice gate narrows from arbitrary physical target pairs to

\[
 \boxed{
 \text{affine-slope dispersal for covers, cocovers, and same-rank
 Johnson pairs.}}
 \tag{5.1}
\]

One possible next refinement is to stratify the nibble simultaneously by
hash colour and affine slope.  The trimmed tag degree is exactly
independent of the affine offset and slope at time zero.  Such
stratification would attack (5.1) directly.  Its hereditary target-degree
and compensator estimates are not proved here.
