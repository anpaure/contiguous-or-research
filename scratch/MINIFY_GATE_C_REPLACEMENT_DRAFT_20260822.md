# Gate C: direct-hole compilation and balanced coset tour banks

This appendix contains only the Gate-C statements used by the live direct
route.  All ground sets and all target sets are labelled.  Throughout,
\(b\) is sufficiently large and odd, so \(H\le b-2\),
\[
 \lvert\Omega\rvert=2b,\qquad
 W=\binom{2b}{b},\qquad
 H=\left\lceil\sqrt{2b\log(2b)}\right\rceil,\qquad
 g=b+H .
 \tag{C.1}
\]
Thus \(H=o(b/\log b)\) and \(g=(1+o(1))b\).

The results below have three roles.

1. A direct-hole compiler turns one literal family of physical fragments
   into a coefficient-one word.
2. Coherent tours and their linear cosets give large integral banks which
   are already disjoint at ranks \(b-1,b,b+1\).
3. The cosets may simultaneously have dual distance greater than \(H\);
   hence every bank has exact \(H\)-wise state balance.

The only unproved assertion is the final boxed selection gate.

## C.1 The direct-hole compiler

A singleton word is a word whose letters are one-element subsets of
\(\Omega\).  For a finite singleton word
\(w=(w_1,\ldots,w_n)\), write
\[
 I_s^w(a)=\{w_a,w_{a+1},\ldots,w_{a+s-1}\}
 \tag{C.2}
\]
when the displayed letters are pairwise distinct.  We call such a window
clean.  A physical \(H\)-fragment of core length \(L\) consists of a
singleton word and \(L\) consecutive core starts for which every window
of length
\[
                       b-H\le s\le b+H                 \tag{C.3}
\]
is contained in the word and clean.  Its designated rank-\(s\) targets
are the \(L\) sets in (C.2) at those core starts.

Consider physical \(H\)-fragments \(F_1,\ldots,F_t\), with core lengths
\(L_1,\ldots,L_t\).  Assume that their designated middle targets are
globally distinct.  Put
\[
 M=\sum_{\ell=1}^tL_\ell,\qquad
 \mathcal I_s=\bigcup_{\ell=1}^t
  \{\text{designated rank-\(s\) targets of }F_\ell\},
 \qquad
 h_s=\binom{2b}{s}-|\mathcal I_s|.                    \tag{C.4}
\]

### Theorem C.1 (direct-hole compiler) [I]/[C]

For every such family, the following finite inequality is [I]:
\[
\boxed{
 \nu(2b)\le
 M+(g-1)t+
 \sum_{s=b-H}^{b+H}h_s+
 \sum_{\substack{1\le s\le2b\\|s-b|>H}}\binom{2b}{s}.}
 \tag{C.5}
\]
Consequently, the following implication is [C]:
\[
 M=W-o(W),\qquad gt=o(W),\qquad
 \sum_{s=b-H}^{b+H}h_s=o(W)                         \tag{C.6}
\]
imply
\[
                         \nu(2b)=(1+o(1))W.          \tag{C.7}
\]

#### Proof

Linearize each fragment separately, retaining its \(L_\ell\) core starts
and the following \(g-1\) singleton letters.  This costs
\(L_\ell+g-1\) letters and realizes every one of its designated targets.
Concatenate the resulting blocks.  No witness is allowed to cross a block
boundary, so repetitions between different blocks are irrelevant.

For every absent band target append one letter equal to that target.
For every nonempty target outside the band do the same.  A one-letter
interval realizes each appended target, proving (C.5).

It remains to bound the far-rank sum.  If
\(X\sim\operatorname {Bin}(2b,1/2)\), the exponential-moment proof of
Hoeffding's bound gives
\[
 \Pr(|X-b|\ge H)\le 2e^{-H^2/b}.
 \tag{C.8}
\]
Also \(W\ge2^{2b}/(2b+1)\), since \(W\) is the largest of the
\(2b+1\) binomial coefficients.  By (C.1),
\[
 \sum_{|s-b|>H}\binom{2b}{s}
 \le2^{2b+1}e^{-H^2/b}=o(W).                        \tag{C.9}
\]
Equations (C.5)--(C.6) give the coefficient-one upper bound.  The central
rank witness lower bound gives \(\nu(2b)\ge W\), so (C.7) follows.
\(\square\)

Theorem C.1 deliberately asks for literal holes, not balanced quotas.
It therefore remains valid when different fragments overlap at
off-middle ranks; only the middle core targets must be disjoint.

## C.2 Coherent FIFO tours

Fix a perfect pairing
\[
 \mathcal P=\{P_j:j\in\mathbb Z_b\},\qquad
 P_j=\{a_j^0,a_j^1\},
 \tag{C.10}
\]
and a directed cyclic order of its pairs.  An initial state
\(x=(x_0,\ldots,x_{b-1})\in\mathbb F_2^b\) selects \(a_j^{x_j}\)
from \(P_j\). The boundary state \(C_{s,0}\) is a FIFO queue, in pair
order \(P_s,P_{s+1},\ldots,P_{s-1}\), containing the currently selected
member of each pair. For \(1\le k<b\), append the opposite member of
\(P_{s+k}\), eject the queue front, and call the resulting middle set
\(C_{s,k}\). Finally append the retained selected member of \(P_s\), eject
the front, and obtain
\[
                         C_{s,b}=C_{s+1,0}.            \tag{C.10a}
\]
Define, for \(1\le k<b\),
\[
 M_{s,k}=C_{s,k},\qquad
 L_{s,k}=C_{s,k}\cap C_{s,k+1},\qquad
 U_{s,k}=C_{s,k}\cup C_{s,k+1}.                    \tag{C.10b}
\]
Thus each packet flips every nonspecial pair once and then rotates the
coordinate queue and special index. Every pair is nonspecial in \(b-1\)
packets; since \(b-1\) is even, the \(b\) packets return both the selected
members and queue order, forming a cyclic tour \(T_{\mathcal P}(x)\).
The cyclic list of appended singleton labels is the tour word, and every
\(C_{s,k}\) above is its current length-\(b\) FIFO window.

Index the internal flags by
\[
                  (s,k),\qquad s\in\mathbb Z_b,\quad
                  1\le k<b,                              \tag{C.11}
\]
and put \(q=b(b-1)\).  The sets in (C.10b) are the attached targets at
ranks \(b-1,b,b+1\). Their
pair-occupancy signatures are
\[
\begin{array}{c|c|c}
\text{target}&\text{empty pairs}&\text{doubled pairs}\\ \hline
L_{s,k}&P_s&\varnothing\\
M_{s,k}&P_s&P_{s+k}\\
U_{s,k},\ k\le b-2&P_s&P_{s+k},P_{s+k+1}\\
U_{s,b-1}&\varnothing&P_{s-1}.
\end{array}                                                \tag{C.12}
\]
Every other pair is split.  On a split pair \(P_j\), the selected member
has the form
\[
                         a_j^{\,x_j+c_{s,k}(j)},             \tag{C.13}
\]
where the chronology constant \(c_{s,k}(j)\in\mathbb F_2\) is independent
of \(x\).  Formulas (C.12)--(C.13) follow directly by recording the pairs
already flipped in the FIFO packet.

Within one tour the middle targets are distinct because their ordered
empty/doubled pair \((P_s,P_{s+k})\) is recoverable.  The lower targets
from different packets have different empty pairs; within one packet
they are successive distinct transversals of a cube path.  The internal
upper signature recovers \(s,k\), and a boundary upper signature has a
different type and recovers \(s\).  Hence one tour has exactly \(q\)
distinct targets separately at all three displayed ranks.

## C.3 Pairing incidence and the necessary pairing scale

A middle target is defect one relative to \(\mathcal P\) if one pair is
empty, a different pair is doubled, and every other pair is split.  The
defect-one stratum has size
\[
 |\mathcal V_{\mathcal P}^{(1)}|
 =b(b-1)2^{b-2}=q2^{b-2},                              \tag{C.14}
\]
because one chooses the ordered empty/doubled pair and one member from
each remaining pair.  Every coherent tour on \(\mathcal P\) uses one
target from each of the \(q\) ordered empty/doubled fibers.

Thus any family of tours on one pairing whose retained middle targets are
disjoint and whose tours each retain at least \((1-\varepsilon)q\)
targets has size at most
\[
                 \frac{2^{b-2}}{1-\varepsilon}.             \tag{C.15}
\]
Any coherent-tour family satisfying the final target (C.41) uses at least
\((1-o(1))W/q\) tours, because one tour supplies at most \(q\) retained
core starts.  If the total number \(D=o(W)\) of deleted starts is nonzero,
put \(\varepsilon_b=\sqrt{D/W}\).  Tours losing more than
\(\varepsilon_bq\) starts number at most
\(D/(\varepsilon_bq)=o(W/q)\); deleting those tours costs only \(o(W)\)
further starts.  The remaining tours satisfy (C.15) with
\(\varepsilon_b=o(1)\).  Consequently any such construction needs
\[
 R\ge(1-o(1))\frac{W}{q2^{b-2}}
       =\Omega\!\left(\frac{2^b}{b^{5/2}}\right)             \tag{C.17}
\]
different pairings.  This is a counting necessity, not a construction.

The complete incidence of pairings with targets is also explicit.  Let
\[
 \mathfrak P=\frac{(2b)!}{2^bb!}.
 \tag{C.18}
\]
A fixed middle target \(C\) is defect one for
\[
\boxed{
 D_1=\binom b2^2(b-2)!=\frac{b!\,b(b-1)}4}
 \tag{C.19}
\]
pairings: choose the internal pair of \(C\), the internal pair of
\(\Omega\setminus C\), and biject the remaining vertices across the cut.
Double counting gives
\[
 p:=\frac{D_1}{\mathfrak P}
   =\frac{q2^{b-2}}{W}.                                  \tag{C.20}
\]

For two targets \(C,D\), put \(d=|C\setminus D|\), \(a=b-d\), and name
their Venn cells
\[
 A=C\cap D,\quad B=C\setminus D,\quad
 G=D\setminus C,\quad E=\Omega\setminus(C\cup D).
\]
Their sizes are \(a,d,d,a\).  Denote an edge between cells \(X,Y\) by
\(XY\), allowing \(X=Y\).  After the small core which
supplies the two defect-one incidences for each cut is removed, all
remaining pairing edges are forced between the two size-\(a\) cells and
between the two size-\(d\) cells.  The exhaustive core list, after
division by the remaining \(a!d!\) bijections, is
\[
\begin{array}{c|c}
AA,EE&a(a-1)/4\\
BB,GG&d(d-1)/4\\
GG,AB,BE;\ BB,AG,GE&ad(d-1)/2\ \text{each}\\
EE,AB,AG;\ AA,BE,GE&da(a-1)/2\ \text{each}\\
AB,AG,BE,GE&a(a-1)d(d-1).
\end{array}                                                \tag{C.21}
\]
The rows partition the four required internal cut incidences according
as two are supplied by one same-cell edge or all are supplied separately;
hence no core is omitted or counted twice.  Summing (C.21) proves that
the common pairing degree is
\[
\boxed{
 \Lambda_d=a!d!\left[
 ad(ad-1)+\frac{a(a-1)+d(d-1)}4\right].}
 \tag{C.22}
\]
Therefore
\[
 \frac{\Lambda_d}{D_1}
 =\frac{4ad(ad-1)+a(a-1)+d(d-1)}
 {b(b-1)\binom bd}.                                      \tag{C.23}
\]
After quotienting \(C\sim\Omega\setminus C\), for \(b\ge7\),
\[
\boxed{
 \max_{1\le d\le(b-1)/2}\frac{\Lambda_d}{D_1}
 =\frac{5(b-2)}{b^2}}                                    \tag{C.24}
\]
attained at \(d=1\).  Substitution gives the displayed value.  For
\(d=2\), the comparison reduces to
\(5b^3-54b^2+179b-186\ge0\).  For \(d\ge3\), use
\(\binom bd\ge\binom b3\) and
\[
 \frac{b^4}{4}+b^2
 \le\frac56(b-1)^2(b-2)^2 .
\]
Both inequalities hold at \(b=7\) and their differences increase
thereafter, proving (C.24).

If \(R\) pairings are sampled uniformly without replacement, a fixed
target is missed with probability at most \(e^{-pR}\).  Hence, for any
arbitrarily slow \(a_b\to\infty\) (in particular \(a_b=o(D_1)\)), some menu of
\[
\boxed{
 R=\left\lceil\frac{a_b}{p}\right\rceil
  =(a_b+o(1))\frac4{\sqrt\pi}\frac{2^b}{b^{5/2}}}
 \tag{C.25}
\]
pairings leaves at most \(We^{-a_b}=o(W)\) targets outside the union of
their defect-one strata. The internal central-binomial estimate (A.1)
and (C.20) give the asymptotic expression. Equations (C.17) and (C.25)
locate the pairing
resource to within the arbitrarily slow factor \(a_b\).

## C.4 Three-rank collision differences

For fixed \(\mathcal P\) and fixed pair order, target membership is affine
in the initial state.  Thus whether \(T_{\mathcal P}(x)\) and
\(T_{\mathcal P}(x')\) collide at one of ranks \(b-1,b,b+1\) depends only
on \(h=x+x'\).  Let
\[
 \mathcal B\subseteq\mathbb F_2^b\setminus\{0\}
 \tag{C.26}
\]
be the set of collision differences.

Equality of two targets first forces equality of their occupancy
signatures in (C.12), and then fixes \(h\) on every split pair.  The
possible equal-signature index pairs and free state bits are
\[
\begin{array}{c|c|c|c}
\text{rank class}&\text{compatible index pairs}
 &\text{free bits}&\text{candidate differences}\\ \hline
b-1&b(b-1)^2&1&2b(b-1)^2\\
b&b(b-1)&2&4b(b-1)\\
b+1\text{ internal}&b(b-2)&3&8b(b-2)\\
b+1\text{ boundary}&b&1&2b.
\end{array}                                                \tag{C.27}
\]
For example, a lower signature fixes the empty pair and leaves only its
state bit free; a middle signature leaves the empty and doubled pair bits
free.  The upper cases are identical.  Internal and boundary upper
signatures cannot agree.  Taking the union in (C.27) gives
\[
\boxed{
 |\mathcal B|\le M_b:=2b^3+8b^2-16b.}
 \tag{C.28}
\]
Moreover \(\mathcal B\) contains every word of Hamming weight one or two.
Indeed, for any ordered \(t\ne i\), two tours share the middle target in
the \((t,i)\)-fiber exactly when their difference is supported on
\(\{t,i\}\).

## C.5 Balanced linear-coset banks

The next theorem strengthens an arbitrary greedy independent bank: all
banks arise as cosets of one code and are exactly balanced on every set
of at most \(H\) state coordinates.

Put
\[
 \rho=\left\lceil\log_2(4M_b)\right\rceil .
 \tag{C.29}
\]
For all sufficiently large \(b\), \(\rho<b\).

### Theorem C.2 (balanced separating code) [I]

More generally than the default value in (C.1), for every integer
\(1\le H=o(b/\log b)\) there is a full-rank linear map
\[
 A:\mathbb F_2^b\longrightarrow\mathbb F_2^\rho
 \tag{C.30}
\]
such that, with \(\mathcal C=\ker A\),
\[
\boxed{
 \mathcal C\cap\mathcal B=\varnothing,\qquad
 d(\mathcal C^\perp)>H.}
 \tag{C.31}
\]
Every coset has
\[
 |\mathcal C|=2^{b-\rho}\ge\frac{2^b}{8M_b}           \tag{C.32}
\]
states.

#### Proof

Choose the \(\rho\) rows of \(A\) independently and uniformly.  For each
nonzero \(h\),
\(\Pr(Ah=0)=2^{-\rho}\), so
\[
 \Pr(\ker A\cap\mathcal B\ne\varnothing)
 \le M_b2^{-\rho}\le\frac14.                         \tag{C.33}
\]
For a fixed nonzero row coefficient
\(u\in\mathbb F_2^\rho\), the word \(uA\) is uniform in
\(\mathbb F_2^b\).  Hence
\[
 \Pr(\exists\,u\ne0:\operatorname {wt}(uA)\le H)
 \le(2^\rho-1)2^{-b}\sum_{j=0}^H\binom bj.           \tag{C.34}
\]
The elementary bound
\[
 \sum_{j=0}^H\binom bj\le(H+1)(eb/H)^H              \tag{C.35}
\]
and \(H=o(b/\log b)\), \(\rho=O(\log b)\), make the logarithm of
the right side \(-(\log2)b+o(b)\).  It is below \(1/4\) for large \(b\).
With positive probability neither bad event occurs.  Avoidance of the
second event also makes the rows independent, because \(uA=0\) would have
weight zero.  Their span is \(\mathcal C^\perp\), proving (C.31).
Finally \(2^\rho<8M_b\), which gives (C.32).
\(\square\)

### Corollary C.3 (three-rank banks and exact resolutions) [I]

For every coset \(z+\mathcal C\),
\[
 \mathfrak B_z=\{T_{\mathcal P}(x):x\in z+\mathcal C\}
 \tag{C.36}
\]
is jointly target-disjoint at ranks \(b-1,b,b+1\).  The cosets resolve
every defect-one middle target exactly four times.

#### Proof

Distinct states in one coset differ by a nonzero word of
\(\mathcal C\), which is outside \(\mathcal B\) by (C.31).  This proves
three-rank disjointness, including within-tour disjointness from C.2.

Fix a defect-one target with empty/doubled pair \((P_t,P_i)\).  Its split
choices determine all state bits outside \(\{t,i\}\), so its four
preimages are
\[
             x_0+\{0,e_t,e_i,e_t+e_i\}.             \tag{C.37}
\]
Every nonzero difference of these states has weight one or two, hence
belongs to \(\mathcal B\) and not to \(\mathcal C\).  The four states
occupy four different cosets, and no other state produces the target.
\(\square\)

The same argument records the adjacent multiplicities.  A lower target
with one empty pair and all others split has \(2(b-1)\) state-index
preimages: there are \(b-1\) positions in its packet and its empty-pair
bit is free.  An accessible internal upper target has eight preimages,
while a packet-boundary upper target has two.  Since any two preimages
share that target, they lie in distinct cosets.  Thus these are also the
exact numbers of coset banks containing the corresponding target.

### Lemma C.4 (dual distance gives exact projections) [I]

If \(J\subseteq[b]\) and \(|J|\le H\), the projection of
\(\mathcal C\) onto \(\mathbb F_2^J\) is surjective.  Every pattern on
\(J\) therefore occurs exactly \(|\mathcal C|/2^{|J|}\) times in every
coset.

#### Proof

If the projection were not onto, a nonzero linear functional on
\(\mathbb F_2^J\) would annihilate it.  Extending the functional by zero
outside \(J\) would give a nonzero word of
\(\mathcal C^\perp\) of weight at most \(H\), contrary to (C.31).
Every fiber of a surjective linear map has the same size, and translation
proves the coset assertion.
\(\square\)

### Theorem C.5 (coset-independent low-order profiles) [I]

Fix the pairing and order.  For every ground-coordinate set
\(S\subseteq\Omega\) with \(|S|\le H\), every coset bank contains the
same number of middle targets containing \(S\).  The same assertion holds
separately at ranks \(b-1\) and \(b+1\).  For one ground coordinate
\(a\),
\[
\boxed{
 |\{T:\ T\text{ is a middle target in }\mathfrak B_z,\ a\in T\}|
 =\frac{q|\mathcal C|}{2}.}
 \tag{C.38}
\]

#### Proof

At a fixed flag index, (C.12)--(C.13) show that containment of \(S\) is
either impossible, automatic on an empty or doubled pair, or prescribes
one state bit for every split pair met by \(S\).  It prescribes at most
\(|S|\le H\) bits.  Lemma C.4 makes the number of solutions independent
of the coset.  Sum over the \(q\) flag indices.  The same proof applies
to the adjacent signatures.

For (C.38), let \(a\in P_j\).  Among the \(q\) middle indices, \(b-1\)
have \(P_j\) empty, \(b-1\) have it doubled, and
\((b-1)(b-2)\) have it split. Averaged uniformly over the coset states,
their contribution is
\[
 0+(b-1)+\frac{(b-1)(b-2)}2=\frac q2.
 \tag{C.39}
\]
Coset independence turns the average into the exact value (C.38).
\(\square\)

Consequently any middle-target-disjoint union of whole coset banks is an
exact one-design: every coordinate lies in half of its selected middle
targets.  Its residual in the full middle layer is also an exact
one-design.  Across different pairings, higher-order profiles can differ.

There is also a useful global codegree consequence. For each pairing and
order, choose a map satisfying Theorem C.2, and then choose a uniform
coset. A fixed defect-one target belongs to four cosets. Two
targets belong to at most four common cosets.  Conditional on the pairing,
their normalized bank codegree is therefore at most one; averaging over
pairings and using (C.23)--(C.24) gives
\[
 \frac{\Pr(C,D\text{ lie in the sampled bank})}
      {\Pr(C\text{ lies in the sampled bank})}
 \le\frac{\Lambda_d}{D_1}
 \le\frac{5(b-2)}{b^2}                                  \tag{C.40}
\]
for noncomplementary targets and \(b\ge7\).  This supplies outer volume
and small pair codegree, but growing bank size prevents a conclusion from
a generic fixed-uniformity matching theorem.

## C.6 Exact remaining independent fragment gate

A repaired coherent-tour fragment is a physical \(H\)-fragment whose
middle core starts are a subset of the ordered flags of one coherent tour
and whose designated targets agree with the attached targets at the
central three ranks.  Splitting one tour into several fragments is
allowed; every split is charged through the fragment count in (C.5).

### Gate \(C_{\rm F}\) [O]

Construct, for every sufficiently large odd \(b\), a family of repaired
coherent-tour fragments drawn from whole balanced coset banks, possibly
followed by deletion of \(o(W)\) total core starts, such that
\[
\boxed{
\begin{aligned}
 &\text{all retained middle core targets are distinct},\\
 &M=W-o(W),\qquad gt=o(W),\\
 &\sum_{s=b-H}^{b+H}
 \left[\binom{2b}{s}-|\mathcal I_s|\right]=o(W).
\end{aligned}}
 \tag{C.41}
\]
Theorem C.1 then proves
\(\nu(2b)=(1+o(1))W\).  The top-bit splice transfers this to the
next three dimensions; since the present base dimensions are
\(2b\equiv2\pmod4\), these bounded transfers cover every sufficiently
large dimension.

The proved input to (C.41) is exact:

* a near-optimal menu of pairings covers all but \(o(W)\) defect-one
  middle targets, by (C.25);
* within every pairing/order, each coset is an integral
  \(2^b/\operatorname {poly}(b)\)-tour bank disjoint at the three central
  ranks;
* all cosets exactly fourfold-resolve the middle stratum and have exact
  adjacent signature loads; and
* every coset is \(H\)-wise uniform, with the pairing-independent
  one-coordinate balance (C.38).

What is not proved is precisely:

1. a target-disjoint selection of whole banks across different pairings
   covering \(W-o(W)\) middle targets while respecting both adjacent
   ranks; and
2. a physical all-offset lift or repair of that same selection whose
   aggregate band-hole sum and fragmentation charge satisfy (C.41).

Neither random pairing coverage, fractional incidence, pair codegree, nor
the low-order balance theorem is being asserted to imply these two
statements.  Conversely, no common symmetric-chain factor is an additional
hypothesis on this direct-hole route: the literal conditions (C.41) are
already sufficient.
