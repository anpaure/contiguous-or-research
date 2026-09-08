# Lane H: PBBS Catalan short-return packing decision

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Verdict

Put

\[
 N=2r+1,\qquad A=\binom Nr,\qquad B=A/N=\operatorname{Cat}_r,
\]

and let (P_r) be the canonical parenthesis/PBBS factor on
(KG(N,r)).  The global assertion

\[
 \nu_H(P_r)=O(B)
 \tag{0.1}
\]

is **not proved or disproved here**.  In particular, this note does not
prove the constant-one contiguous-OR theorem.

The proposed local Catalan-quotient proof of (0.1) is, however, false inside
the actual PBBS.  For every $r\ge3$ there is one genuine PBBS component of
length $3N$ containing $r$ pairwise step-two-edge-disjoint gap-five
return arcs, all having the same trace in the cyclic-coordinate quotient.
Consequently no bounded-menu assignment which factors through the rotation
quotient has bounded congestion.

Two further aggregate theorems sharply delimit this obstruction.

1. If $d(D)=r-\operatorname{pk}(D)$ is the peak defect of the normalized
   Dyck root, then $d$ is PBBS-invariant and its class has the exact
   Narayana size

   \[
   \frac1r\binom rd\binom r{d+1}.
   \tag{0.2}
   \]

   Hence all physical PBBS states with $d\le D_r$ have total cardinality
   $o(B)$ whenever $D_r=o(r/\log r)$.  In particular, every
   $O(H)$-defect decoration of the bad $3N$-component is negligible in
   the required range

   \[
   H=\sqrt m\,\omega(m),\qquad
   \omega\to\infty,\qquad
   \omega=o(\sqrt m/\log ^2m),\qquad r=m-1.
   \tag{0.3}
   \]

2. All quotient cycles of period $O(H)$, with all their physical lifts,
   also have total cardinality $o(B)$.  Thus bounded-period amplification
   of the explicit component is impossible.

For definiteness put \(Q_r=\lceil H\log r\rceil\).  In (0.3),
\(Q_r=o(r/\log r)\).  After the two aggregate theorems, the smallest
remaining packing statement is the high-defect, long-period assertion

> every edge-disjoint packing of return arcs of gap at most $2H-1$ whose
> initial normalized roots have $d\ge H$ and whose quotient cycles have
> period greater than \(Q_r\) has size $O(B)$.

A stronger, very clean sufficient lemma is

\[
 \boxed{g\ge 2d(D)+1=N-2\operatorname{pk}(D)}
 \tag{0.4}
\]

for every consecutive omitted-label return of gap $g$.  This lemma is
**UNPROVED**.  If true, (0.2) makes the entire short-return family $o(B)$,
not merely its maximum packing.  The constant in (0.4) is sharp: an explicit
$r=6$ PBBS orbit below has a consecutive return with equality $g=7$.

## 1. The exact rooted-Dyck PBBS map

Use $1$ for an up-step and $0$ for a down-step.  Rotate a PBBS state so
that its unique unmatched zero has coordinate (u) and occurs just before a
Dyck word (D) of semilength (r).  If the first up-step attaining the
maximum height of (D) is displayed as

\[
 D=P,1,Q,
\]

put

\[
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q\,0\,\overline P,
 \tag{1.1}
\]

where the bar interchanges zero and one.

### Lemma 1.1 (exact skew product)

The word $\phi(D)$ is Dyck and one PBBS step is

\[
 (u,D)\longmapsto
 (u+\delta(D)\pmod N,\phi(D)).
 \tag{1.2}
\]

#### Proof

Let the marked up-step first attain height $h$.  Along $Q$, the old
height never exceeds $h$ and ends at zero.  Consequently the complemented
suffix $\overline Q$, started at height zero, has nonnegative partial sums
and ends at height $h$.  The displayed zero lowers the height to $h-1$.
Every prefix of $P$ has height at most $h-1$, so $\overline P$, started
at height $h-1$, remains nonnegative and ends at zero.  Thus $\phi(D)$ is
Dyck.

The PBBS update fixes the unmatched zero and complements every bit of $D$.
In the resulting cyclic word $0\overline D$, the complemented marked
up-step is the new unmatched zero.  Its coordinate is $u+|P|+1$, and
cutting there reads $\overline Q0\overline P$.  This proves (1.2).
\(\square\)

Every directed PBBS factor edge is therefore represented uniquely by one
pair

\[
 (u,D)\in\mathbb Z_N\times\mathcal D_r,
 \tag{1.3}
\]

where $\mathcal D_r$ is the $B$-element set of Dyck words of semilength
$r$.

## 2. The Catalan quotient and the actual local-injection obstruction

### Lemma 2.1 (the rotation quotient has exactly \(B\) edges)

Cyclic coordinate rotation acts freely on the \(r\)-subsets of
\([N]\), hence freely on directed PBBS transition edges.  The quotient has
exactly \(A/N=B\) directed transition-edge certificates.

#### Proof

If a nonidentity rotation fixed an \(r\)-set, that set would be a union of
cycles of some common length \(s>1\) dividing \(N\).  Then \(s\mid r\),
contrary to

\[
 \gcd(N,r)=\gcd(2r+1,r)=1.
\]

A fixed directed transition edge would in particular have a fixed source,
so the edge action is also free.  There are \(A\) directed transitions in
the factor.  Division by \(N\) proves the claim.  \(\square\)

### Theorem 2.2 (a genuine \(3N\)-component defeats local quotient packing)

For every \(r\ge3\), the canonical PBBS factor contains a component of
length \(3N\) with \(r=\lfloor N/2\rfloor\) pairwise disjoint projected
residence intervals of gap five.  All \(r\) intervals have the same
four-occurrence ordered cyclic-coordinate quotient trace; the support of
that trace consists of three directed quotient-transition classes, one
class occurring twice.

#### Proof

Consider

\[
\begin{aligned}
 D_0&=11(01)^{r-2}00,\\
 D_1&=(10)^{r-2}1100,\\
 D_2&=110(01)^{r-2}0.
\end{aligned}
\tag{2.1}
\]

All three words are Dyck.  Their first maximum-attaining up-steps occur at
positions

\[
 2,\qquad 2r-2=N-3,\qquad 2.
\tag{2.2}
\]

Direct substitution in (1.1) gives

\[
 D_0\xrightarrow{\,2\,}D_1
 \xrightarrow{\,N-3\,}D_2
 \xrightarrow{\,2\,}D_0.
\tag{2.3}
\]

For example, in the first step

\[
 \overline{(01)^{r-2}00}\,0\,\overline1
 =(10)^{r-2}1100,
\]

and the other two identities are identical literal substitutions.  The
three-step voltage is \(N+1\equiv1\pmod N\).  Hence the lift of (2.3) is one
component of length \(3N\); after three steps it advances the ground labels
by one.

Starting in phase \(D_0\), the first five positive voltage sums are

\[
 2,\quad N-1,\quad N+1,\quad N+3,\quad 2N.
\tag{2.4}
\]

None of the first four is zero modulo \(N\), while the fifth is.  Thus every
one of the \(N\) spatial lifts of phase \(D_0\) starts a consecutive
omitted-label return of gap five.  Its projected positive residence is
three, and its interval consists of the four step-two transition edges

\[
 I_j=\{i_j-1,i_j+1,i_j+3,i_j+5\},
 \qquad i_j=i_0+3j,\quad j\in\mathbb Z_N.
\tag{2.5}
\]

Writing an edge of \(I_j\) as \(i_0+3j-1+2h\), \(0\le h\le3\), shows

\[
 I_j\cap I_k\ne\varnothing
 \quad\Longleftrightarrow\quad
 j-k\equiv0,\pm2\pmod N.
\tag{2.6}
\]

Because \(N\) is odd, the nontrivial conflict graph generated by
\(j\mapsto j\pm2\) is one \(N\)-cycle.  Its independence number is
\(\lfloor N/2\rfloor=r\), proving the packing claim.

Ground rotation by one is time translation by three on this component.
Therefore all intervals (2.5) have the same rotation quotient.  Their four
edge positions have residues \(-1,1,0,2\equiv-1\pmod3\), so their quotient
trace has exactly three directed transition classes.  \(\square\)

### Corollary 2.3 (no bounded local quotient-certificate menu)

Let $\Gamma(I)$ be a menu of cyclic-coordinate quotient certificates
determined by the quotient trace of $I$, and assume
$|\Gamma(I)|\le K$ for a constant $K$.  There is no assignment of every
member of every disjoint PBBS return-arc family to a member of its menu with
constant congestion.

#### Proof

Apply the assignment to the $r$ disjoint intervals of Theorem 2.2.  Their
menus are identical, so some one of the at most $K$ certificates receives
at least $\lceil r/K\rceil$ intervals.  This diverges with $r$.
\(\square\)

Thus “inject into Catalan quotient certificates” has two possible precise
meanings.  An unrestricted injection into $O(1)$ copies of an abstract
$B$-set is simply a restatement of (0.1).  The nonvacuous local quotient
meaning is false by Corollary 2.3.

Theorem 2.2 is not by itself a counterexample to (0.1), since (r=o(B)).
The next two sections prove that it cannot be amplified by the most direct
decorations.

## 3. Peak defect is invariant and low-defect mass is negligible

For $D\in\mathcal D_r$, let $\operatorname{pk}(D)$ be the number of
occurrences of $10$, and put

\[
 d(D)=r-\operatorname{pk}(D),
 \qquad
 p(D)=2d(D)+1=N-2\operatorname{pk}(D).
\tag{3.1}
\]

### Lemma 3.1 (exact PBBS invariance)

Both $d(D)$ and $p(D)$ are invariant under $\phi$.

#### Proof

In the rooted cyclic word \(0D\), the number of \(10\)-edges and the number
of \(01\)-edges are both \(\operatorname{pk}(D)\).  Hence the number of equal
cyclic adjacencies is \(N-2\operatorname{pk}(D)=p(D)\).

Under one PBBS update all bits except the unmatched root zero are
complemented.  Every adjacency not incident with the root preserves its
equality status.  The edge immediately before the root is (00) and becomes
unequal, while the edge immediately after the root is (01) and becomes
(00).  Exactly one equal edge is removed and one is created.  Thus their
number, and hence \(p\) and \(d\), is invariant.  \(\square\)

### Lemma 3.2 (exact Narayana class size)

For \(0\le d\le r-1\),

\[
 \#\{D\in\mathcal D_r:d(D)=d\}
 =\frac1r\binom rd\binom r{d+1}.
\tag{3.2}
\]

#### Proof

Let \(C(z,u)\) be the generating function in which \(z\) marks semilength
and \(u\) marks peaks.  The first-return decomposition \(D=1E0F\) gives

\[
 C=1+zuC+z(C-1)C
   =1+zC(C+u-1).
\tag{3.3}
\]

Indeed, \(E=\varnothing\) creates the displayed peak, while
\(E\ne\varnothing\) does not.  Put \(Y=C-1\).  Then

\[
 Y=z(1+Y)(u+Y).
\]

Lagrange inversion yields

\[
 [z^ru^k]Y
 =\frac1r[t^{r-1}u^k](1+t)^r(u+t)^r
 =\frac1r\binom rk\binom r{k-1}.
\tag{3.4}
\]

Substitute \(k=r-d\) and use binomial symmetry.  \(\square\)

### Theorem 3.3 (low-defect aggregate theorem)

Let \(D_r=o(r/\log r)\).  The total number of physical PBBS states whose
normalized Dyck root satisfies \(d(D)\le D_r\) is \(o(B)\).  Consequently
the total number, packed or otherwise, of return arcs starting in those
states is \(o(B)\), uniformly in their gaps.

#### Proof

For \(D_r\le r/2-1\), monotonicity of the binomial coefficients and (3.2)
give

\[
\begin{aligned}
 R_r(D_r)
 &:=\sum_{d\le D_r}\frac1r\binom rd\binom r{d+1}\\
 &\le (D_r+1)
       \left(\frac{er}{D_r+1}\right)^{2(D_r+1)}.
\end{aligned}
\tag{3.5}
\]

Therefore

\[
 \log R_r(D_r)
 =O\!\left(D_r\log\frac r{D_r}+\log r\right)=o(r).
\tag{3.6}
\]

On the other hand, since the central binomial coefficient is the largest of
the (2r+1) binomial coefficients of order (2r),

\[
 B=\operatorname{Cat}_r
 =\frac1{r+1}\binom{2r}r
 \ge\frac{4^r}{(r+1)(2r+1)}.
\tag{3.7}
\]

There are exactly \(N\) physical roots over each \(D\).  Equations
(3.5)--(3.7) therefore give

\[
 N R_r(D_r)=\exp(o(r))=o(B).
\]

At most one positive-residence return arc starts at a directed transition
edge, so the same bound holds for all arcs starting in these states.
\(\square\)

For (0.3), every fixed multiple \(D_r=CH\) satisfies the hypothesis of
Theorem 3.3.  Thus the explicit \(d=1\) component of Theorem 2.2 and every
\(O(H)\)-defect decoration of it are globally negligible.

## 4. Bounded quotient periods are also negligible

### Theorem 4.1 (voltage-itinerary rigidity)

Let $D_0,\ldots,D_{q-1}$ be a quotient $\phi$-cycle and set

\[
 a_j=\delta(D_j),\qquad S=\sum_{j=0}^{q-1}a_j.
\]

The ordered cyclic voltage itinerary \((a_0,\ldots,a_{q-1})\) determines
the quotient cycle up to its choice of starting phase.  Consequently the
number of quotient states lying on cycles of period at most \(Q\) is at most

\[
 QN^Q.
\tag{4.1}
\]

#### Proof

Fix the initial omitted label to be zero.  The itinerary determines the full
periodic omitted-label word by

\[
 \lambda_0=0,
 \qquad
 \lambda_{t+1}=\lambda_t+a_{t\bmod q}\pmod N.
\tag{4.2}
\]

A valid PBBS omitted-label word determines all factor states.  Here we use
the established componentwise complete-colour theorem: every ground label
occurs in every lifted PBBS component.  At an
\(x\)-labelled edge, \(x\) is absent from both incident states.  Until the
next \(x\)-edge its membership alternates at every step.  Consecutive
\(x\)-gaps are odd, so these prescriptions are consistent at their two ends.
Doing this for every coordinate reconstructs every bit of every state, and
hence reconstructs \(D_0\).

There are fewer than \(N^q\) ordered length-\(q\) voltage words.  Summing this
bound over \(q\le Q\) proves (4.1).  \(\square\)

### Corollary 4.2 (no short-period amplification)

If \(Q=o(r/\log r)\), then all quotient cycles of period at most \(Q\), with
all their physical lifts, contain \(o(B)\) transitions and hence support
only \(o(B)\) return arcs.

#### Proof

Multiplying (4.1) by the \(N\) spatial roots gives at most

\[
 NQN^Q=\exp(o(r))=o(B)
\]

by (3.7).  \(\square\)

In particular every \(Q=o(r/\log r)\) is harmless.  With
\(Q_r=\lceil H\log r\rceil\), any counterexample to (0.1) must therefore use
high-defect roots on quotient cycles of period greater than \(Q_r\), not
merely greater than a fixed multiple of \(H\).

## 5. The exact remaining lemma and its quantitative implication

### Vacancy-gap lemma -- UNPROVED

For every normalized root (D) and every consecutive omitted-label return
of gap (g),

\[
 \boxed{g\ge p(D)=2d(D)+1.}
\tag{5.1}
\]

If (5.1) holds and \(g\le2H-1\), then \(d(D)\le H-1\).  Theorem 3.3, with
\(D_r=H-1\), would give

\[
 |\mathcal I_H|=o(B),
 \qquad
 \nu_H(P_r)\le|\mathcal I_H|=o(B).
\tag{5.2}
\]

For \(r=m-1\), \(A_m=(2m-1)B\), and (0.3),

\[
 \frac{B}{A_m/(H\log m)}
 =\frac{H\log m}{2m-1}=o(1).
\tag{5.3}
\]

Thus (5.1) would prove the residence estimate required by the pair-omission
PBBS construction, with room to spare.

Without (5.1), combine Theorem 3.3 with Corollary 4.2 at
\(Q_r=\lceil H\log r\rceil\).  The smallest exact replacement left by both
aggregate theorems is:

> **High-defect long-period packing lemma -- UNPROVED.**  Uniformly in (0.3), every
> pairwise edge-disjoint family of return arcs of gap at most \(2H-1\)
> whose initial roots satisfy \(d(D)\ge H\), and which lie on quotient cycles
> of period greater than \(Q_r\), has size \(O(B)\).

This is strictly weaker than (5.1), and it is exactly what remains after the
unconditional low-defect and short-period arcs are discarded.

## 6. Sharp adversarial audit

The most tempting attempted proof of (5.1) was a false primitive-height
claim.  The following example records both the failure and the sharpness of
the surviving vacancy scale.

Take

\[
 r=6,\qquad N=13,\qquad D_0=111001100100.
\tag{6.1}
\]

This is a primitive Dyck word of height three, with three peaks, so

\[
 d(D_0)=3,qquad p(D_0)=7.
\tag{6.2}
\]

Literal use of (1.1) gives the initial orbit

\[
\begin{array}{c|c}
t&D_t\quad\text{and}\quad\delta(D_t)\\ \hline
0&111001100100\quad 3\\
1&110011011000\quad 9\\
2&111000110010\quad 3\\
3&111001101000\quad 3\\
4&110010111000\quad 9\\
5&111000110100\quad 3\\
6&111001011000\quad 3\\
7&110100111000\quad 9.
\end{array}
\tag{6.3}
\]

Starting in phase \(t=0\), the sum of the first seven voltages is \(33\),
not zero modulo \(13\).  Thus the false assertion that every primitive word
of height \(h\) returns after \(2h+1\) steps already fails here.

Starting instead in phase \(t=1\), the seven voltages are

\[
 9,3,3,9,3,3,9.
\]

Their proper partial sums modulo (13) are

\[
 9,12,2,11,1,4,
\]

while their full sum is (39=3N).  Hence this is a consecutive return of
gap

\[
 g=7=p(D_0).
\tag{6.4}
\]

Therefore no universal strengthening of (5.1) to \(g\ge p+2\) is possible.
The candidate (5.1), if true, is sharp.

The audit conclusions are consequently exact.

1. Theorem 2.2 disproves only local quotient bounded-menu
   quotient certification.  Its (r) arcs are (o(B)), so it does not
   disprove the numerical packing theorem.
2. Theorems 3.3 and 4.1 are aggregate enumeration statements, not packing
   proofs for high-defect long quotient cycles.
3. Primitive height is not the controlling invariant.  Peak defect is
   invariant, but the key return inequality (5.1) remains unproved.
4. The upper restriction on $\omega$ in (0.3) is used in both the
   Narayana and final quantitative estimates; the phrase
   \(H=\sqrt m\,\omega\) without that restriction is insufficient.

Accordingly, the requested global PACKING theorem remains open.  The
specified natural quotient-injection mechanism is rigorously closed by an
actual PBBS component, and the remaining possible proof or counterexample
is confined to the high-defect, long-quotient sector stated above.
