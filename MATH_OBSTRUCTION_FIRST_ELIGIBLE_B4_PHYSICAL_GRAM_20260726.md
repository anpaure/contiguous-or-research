# Physical Gram obstruction for first-eligible \(B_4\) packets

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input
is used.

## 0. Verdict

Let

\[
 \mathcal A_0=\{14,12,23,34\}
\]

be the fixed cyclic \(B_4\) seed, and form \(Q_{2r}\)-packets from the first
\(r\) eligible four-blocks.  At signed depth \(q\), one packet has

\[
 F_{r,q}=2^{2r-q}\binom{2r}{q}                       \tag{0.1}
\]

affine candidate faces.  If \(d_q(T)\) is the number of distinct packets
whose candidate family contains the physical target \(T\), then the entire
cross-packet overlap is exactly

\[
 \sum_{a\ne b}|\mathcal B_{a,q}\cap\mathcal B_{b,q}|
 =\sum_Td_q(T)(d_q(T)-1).                             \tag{0.2}
\]

There is an exact subdegree of \(d_q\) which already obstructs the proposed
mesoscopic scale.  Put \(k=r-q\).  Scan the physical four-blocks in their
fixed order and, for a lower target \(T\), let \(S_k(T)\) be the number of
singleton blocks before the \(k\)-th block whose local state lies in
\(\mathcal A_0\).  Then

\[
 \boxed{D_q(T):=\binom{S_k(T)}q\le d_q(T).}           \tag{0.3}
\]

Every term in (0.3) is a literal candidate in a different first-eligible
packet: select the indicated \(q\) singleton blocks, complete each through
its unique edge of the local four-cycle, leave the first \(k\) genuine
eligible blocks untouched, and stop at the \(k\)-th one.

Under the Bernoulli measure of density

\[
 \rho={m-q\over2m},
\]

the untruncated stopping variable \(S_k\) is negative binomial with \(k\)
successes and success parameter \(\rho\).  The physical stream has only
\(b\) blocks; its exact truncation is already included in the transfer
(2.4), and differs from the following moments by an exponentially negligible
term in the stated range.  Consequently, with

\[
 \vartheta={1-\rho\over\rho},
\]

its factorial moments give the exact identities

\[
 \mathbb ED_q={ (k)^{\overline q}\vartheta^q\over q!},                 \tag{0.4}
\]

and

\[
 \mathbb ED_q^2
 ={1\over(q!)^2}\sum_{\ell=0}^q
   \binom q\ell^2\ell!\,(k)^{\overline{\,2q-\ell\,}}
   \vartheta^{\,2q-\ell}.                            \tag{0.5}
\]

In particular, the \(\ell=0\) summand is a positive coherent overlap mode.
After conditioning on the physical target rank, it yields, whenever

\[
 q=O(\sqrt m),\qquad q=o(r),\qquad r=o(m),             \tag{0.6}
\]

the normalized second-moment bound

\[
 {N_q^{-1}\sum_Td_q(T)^2\over
  \left(N_q^{-1}\sum_Td_q(T)\right)^2}
 \ge
 \exp\left\{
    {q^2\over2r}
    -O\left({q^3\over r^2}+{q^2\over m}+{q\over r}+1\right)
 \right\}.                                           \tag{0.7}
\]

Thus, if \(q^2/r\to\infty\),

\[
 \boxed{\eta_q\ge
 \exp\bigl((1/2-o(1))q^2/r\bigr)-1,}                 \tag{0.8}
\]

where \(\eta_q\) is the positive physical Gram excess.  At the advertised
choice \(r\asymp m^{3/4}\) and any fixed Gaussian depth
\(q=x\sqrt m\), \(x>0\),

\[
 \eta_q\ge \exp\bigl((x^2/2+o(1))m^{1/4}\bigr)-1.    \tag{0.9}
\]

The desired condition \(\sum_q\sqrt{\eta_q}=o(1)\) therefore fails already
in one row, by an exponential margin.  In coefficient language, the fixed
first-eligible seed would require \(H^2/r=o(1)\); at Gaussian depth
\(H=\Theta(\sqrt m)\), this asks for \(r\gg m\), outside the construction.

This conclusion is not caused by allowing too many affine candidates.  If
one keeps only sibling-compatible faces which touch at most one direction
in each local \(B_4\), the packet candidate count becomes

\[
 F^{\rm nr}_{r,q}
 =\binom rq2^q2^{2r-q}=2^{2r}\binom rq.              \tag{0.10}
\]

The subdegree (0.3) is entirely contained in this no-repeat family.  With
the smaller mean \((G/N_q)\binom rq\), the leading exponent in (0.7) is
\(q^2/r\), rather than \(q^2/(2r)\).  Thus the actual sibling-block
restriction strengthens the obstruction.

The three relabelled \(B_4\) seeds do not automatically repair this.
All three have exactly the same singleton and triple boundary alphabets, so
the mode (0.3)--(0.5) is present for every fixed seed.  A global seed
relabeling or global block permutation merely relabels the target layer and
leaves the Gram sum unchanged.  A permutation of the active cube directions
does even less: the set of all affine \(q\)-faces is invariant, hence its
candidate family is literally unchanged.

Most importantly, changing the seed of one existing packet is not an
owner-preserving catalogue choice.  Two different four-cycles have different
four-element middle supports.  Switching seeds removes some owners of the
packet and imports others.  Fractionally averaging the three complete
packetizations uses three owner copies, not coefficient one.

Accordingly, the only possible escape is a new context-dependent integral
repacketization which simultaneously proves owner disjointness and suppresses
the stopping statistic \(S_k\).  The exact residual lemma is stated in
Section 7.  It is strictly stronger than choosing one of three labels
independently in each old packet.

## 1. The three local seeds

The three Hamilton four-cycles in \(J(4,2)\), up to orientation, are the
complements of the three antipodal pairs:

\[
\begin{aligned}
 \mathcal A_0&=\binom{[4]}2\setminus\{13,24\},\\
 \mathcal A_1&=\binom{[4]}2\setminus\{12,34\},\\
 \mathcal A_2&=\binom{[4]}2\setminus\{14,23\}.
\end{aligned}                                         \tag{1.1}
\]

For example their cyclic orders may be taken as

\[
\begin{aligned}
 &14,12,23,34,\\
 &13,14,24,23,\\
 &12,13,34,24.
\end{aligned}                                         \tag{1.2}
\]

In every row of (1.2), the four lower edge labels are the four singletons,
once each, and the four upper labels are the four triples, once each.
Moreover,

\[
 \sum_{\sigma=0}^2 1_{\{A\in\mathcal A_\sigma\}}=2
 \quad\text{for every }A\in\binom{[4]}2.             \tag{1.3}
\]

Identity (1.3) explains why the *fractional* three-seed average looks flat.
It does not supply an integral owner factor.

## 2. Exact candidate-degree automaton

The following finite transfer gives the complete fixed-seed candidate
overlap, not merely the subdegree (0.3).

For a local target state \(A\subseteq[4]\), let
\(M_\sigma(A)\) act on states \((c,w)\), where \(0\le c\le r\) is the
number of selected eligible blocks and \(0\le w\le q\) is the accumulated
codimension.  State \(c=r\) is absorbing.  Before absorption the legal
transitions are

\[
\begin{array}{c|c}
 A\in\mathcal A_\sigma &(c,w)\mapsto(c+1,w),\\
 |A|=1 &(c,w)\mapsto(c,w)\text{ or }(c+1,w+1),\\
 A=\varnothing &(c,w)\mapsto(c,w)\text{ or }(c+1,w+2),\\
 \text{otherwise} &(c,w)\mapsto(c,w).
\end{array}                                           \tag{2.1}
\]

Transitions outside the displayed ranges are deleted.  If
\(T_i=T\cap B_i\), then the exact lower candidate degree is

\[
 d_{\sigma,q}(T)
 =\langle r,q|M_\sigma(T_b)\cdots M_\sigma(T_1)|0,0\rangle.             \tag{2.2}
\]

For two seeds define the common-target tensor transfer

\[
 \mathscr M_{\sigma,\tau}(z)
 =\sum_{A\subseteq[4]}z^{|A|}
   M_\sigma(A)\otimes M_\tau(A).                     \tag{2.3}
\]

If \(s_0=2m-4b\) coordinates lie outside the four-blocks, then

\[
\begin{split}
 \sum_{|T|=m-q}d_{\sigma,q}(T)d_{\tau,q}(T)
  =[z^{m-q}](1+z)^{s_0}\,
  \langle r,q;r,q|\mathscr M_{\sigma,\tau}(z)^b
  |0,0;0,0\rangle .                                  \tag{2.4}
\end{split}

Equations (0.2) and (2.4) are the requested exact computation of all
cross-packet candidate overlaps for the fixed seed.  Complementation gives
the identical upper formula.

Notice that (2.4) uses physical target identities.  It is not a
pair-type or marginal calculation.

## 3. The singleton stopping subkernel

Take \(k=r-q\).  Consider only paths in (2.1) which

1. select exactly the first \(k\) encountered \(\mathcal A_\sigma\)-blocks;
2. select exactly \(q\) singleton blocks before the \(k\)-th such block;
3. use no empty block.

The last selected event is the \(k\)-th genuine eligible block, so these
are legal first-\(r\)-eligible histories of codimension \(q\).  A singleton
has a unique completion edge in every cycle (1.2).  Hence distinct choices
of singleton blocks give distinct packets and distinct affine faces.  This
proves (0.3).

Under product density \(\rho\), a fixed block is of type
\(\mathcal A_\sigma\) with probability

\[
 a=4\rho^2(1-\rho)^2,                                 \tag{3.1}
\]

and is a singleton with probability

\[
 s=4\rho(1-\rho)^3.                                  \tag{3.2}
\]

After deleting all other block types, the probability that the next retained
event is an \(\mathcal A_\sigma\)-event is exactly

\[
 {a\over a+s}=\rho.                                   \tag{3.3}
\]

Thus the infinite-stream \(S_k\) is negative binomial.  Its factorial
moments are

\[
 \mathbb E(S_k)_{\underline t}
 =(k)^{\overline t}\vartheta^t.                      \tag{3.4}
\]

Using

\[
 (x)_{\underline q}^2
 =\sum_{\ell=0}^q\binom q\ell^2\ell!
   (x)_{\underline{2q-\ell}}                         \tag{3.5}
\]

proves (0.4)--(0.5).  This is the precise positive coefficient: the
\(\ell=0\) term counts two disjoint chosen singleton sets before a common
stopping event.

For the finite physical stream, the exact expression is obtained by stopping
the one-history or two-history transfer at power \(b\), as in (2.4).  Since
\(r\le m/16\), the expected number of \(\mathcal A_\sigma\)-blocks is at
least twice \(r\).  Chernoff's exponential-moment argument, also after the
factorial tilts of order at most \(2q=o(m)\), shows that truncation changes
(0.4)--(0.5) by \(\exp(-\Omega(m))\) relative error.

For the upper sign use target density \(\rho=(m+q)/(2m)\).  The competing
boundary events are triples, of probability \(4\rho^3(1-\rho)\), and the
conditional success parameter is \(1-\rho=(m-q)/(2m)\).  Therefore the same
formulas result.

## 4. Conditioning on the physical rank

For completeness, the coefficient transfer from product measure to the
fixed target layer is recorded here.

### Lemma 4.1 (rank-conditioning comparison)

Assume (0.6), and restrict the negative-binomial sum to

\[
 |S_k-k\vartheta|\le C(q+\sqrt r).                    \tag{4.1}
\]

For every fixed sufficiently large \(C\), the omitted part is a fixed
exponentially small fraction under each factorial tilt occurring in the
\(\ell=0\) term.  On (4.1), conditioning the total coordinate count to
\(m-q\) changes the remaining-coordinate coefficient by at most

\[
 \exp O\left({q^2+r\over m}+1\right).                 \tag{4.2}
\]

The same statement holds at the upper rank.

#### Proof

The factorial tilt of order \(2q\) changes a negative-binomial law with
\(k\) successes into the corresponding law with \(k+2q\) successes, times
an explicit constant; its mean moves by \(O(q)\) and its variance remains
\(\Theta(r+q)\).  Chernoff's elementary exponential-moment proof gives the
first assertion.

The stopped prefix contains \(O(r+q)\) relevant blocks with exponentially
small tails.  In (4.1), its coordinate-count displacement from its tilted
mean is \(O(q+\sqrt r)\).  The unused \(2m-O(r)\) coordinates have variance
\(\Theta(m)\).  Taking the ratio of their two adjacent binomial coefficients,
and multiplying those ratios from the mean to the required displacement,
gives

\[
 \log {\Pr\{R=n-\Delta\}\over\Pr\{R=n\}}
 =O\left({\Delta^2\over m}+1\right)
 =O\left({q^2+r\over m}+1\right).
\]

This proves (4.2) without an independence assumption between packets.
\(\square\)

At the mesoscopic scale \(r=o(m)\), the conditioning loss in (4.2) is
\(\exp\{O(q^2/m+1)\}\), whereas the obstruction below has exponent
\(q^2/r\).

## 5. Normalization against the full candidate mean

Let \(P\) be the number of retained packets and \(G=P2^{2r}\) their number
of middle owners.  Since a packet has (0.1) candidate faces,

\[
 \bar d_q:={1\over N_q}\sum_Td_q(T)
 ={G\over N_q}{\binom{2r}{q}\over2^q}.                \tag{5.1}
\]

At Gaussian depth \(G/N_q=\exp\{O(q^2/m)+o(1)\}\).  The \(\ell=0\) term
of (0.5), Lemma 4.1, and (5.1) give

\[
\begin{split}
 \log {N_q^{-1}\sum_Td_q(T)^2\over\bar d_q^2}
 &\ge
 \log{(r-q)^{\overline{2q}}\over(q!)^2}
 -2\log\left({\binom{2r}{q}\over2^q}\right)\\
 &\qquad-O\left({q^2\over m}+{r\over m}+1\right).    \tag{5.2}
\end{split}

The elementary product expansions

\[
 \log (r-q)^{\overline{2q}}
 =2q\log r-O\left({q\over r}+{q^3\over r^2}\right),  \tag{5.3}
\]

and

\[
 2\log\left({\binom{2r}{q}\over2^q}\right)
 =2q\log r-2\log(q!)-{q(q-1)\over2r}
  +O(q^3/r^2)                                         \tag{5.4}
\]

prove (0.7).  The leading \(q^2/(2r)\) is not a Gaussian heuristic; it is
the coefficient difference between the symmetric rising product in (5.3)
and the falling product in (5.4).

For the no-repeat catalogue (0.10), (5.1) is replaced by

\[
 \bar d_q^{\rm nr}={G\over N_q}\binom rq.             \tag{5.5}
\]

Since

\[
 2\log\binom rq
 =2q\log r-2\log(q!)-{q(q-1)\over r}
  +O(q^3/r^2),                                        \tag{5.6}
\]

the same calculation gives

\[
 \log {N_q^{-1}\sum_T(d_q^{\rm nr}(T))^2
              \over(\bar d_q^{\rm nr})^2}
 \ge {q^2\over r}
 -O\left({q^3\over r^2}+{q^2\over m}+{q\over r}+1\right).            \tag{5.7}
\]

Here \(d_q^{\rm nr}\ge D_q\), because every history counted by \(D_q\)
touches one direction in each of \(q\) distinct singleton blocks.

## 6. Conversion to physical Gram excess

Write \(K_q=F_{r,q}\).  Then

\[
\begin{split}
 R_q
 &=\sum_Td_q(T)(d_q(T)-1)-{P(P-1)K_q^2\over N_q}\\
 &=N_q\bar d_q^2
   \left(
    {N_q^{-1}\sum_Td_q(T)^2\over\bar d_q^2}-1
   \right)
   -P K_q+{P K_q^2\over N_q}.                         \tag{6.1}
\end{split}

Here \(\bar d_q\to\infty\) in the range under discussion, so the last two
terms are negligible relative to \(N_q\bar d_q^2\).  Since

\[
 {P(P-1)K_q^2\over N_q}=(1+o(1))N_q\bar d_q^2,        \tag{6.2}
\]

(0.8) follows from (0.7).  The positive-correlation residual appearing in
the physical Gram estimate therefore has size at least

\[
 G\sqrt{\eta_q}
 \ge G\exp\bigl((1/4-o(1))q^2/r\bigr)                \tag{6.3}
\]

in this one row.  Hence the positive-overlap condition required by that
Gram route cannot be \(o(W)\).  This is an obstruction to the candidate-Gram
proof, not by itself a lower bound against every possible direct selection
of consecutive windows.

## 7. Why the apparent catalogue is not legal

There are two separate invariance statements.

### 7.1 Direction and block permutations

The candidate family of a \(Q_{2r}\)-cell consists of *all* affine
codimension-\(q\) faces.  Every permutation or conjugation of its active
directions permutes these faces and leaves their union as a physical target
family unchanged.  Hence such a choice can alter the eventual consecutive
windows, but cannot alter \(d_q(T)\), (2.4), \(R_q\), or \(\eta_q\).

If only sibling-compatible permutations are admitted, the no-repeat family
(0.10) is likewise invariant under block permutations and independent swaps
of the two directions inside a block.  Its stronger coefficient (5.7) is
therefore also unaffected.

A single global permutation of the physical four-block order also merely
relabels all targets, so the summed Gram coefficient (2.4) is invariant.

### 7.2 Seed changes

For \(\sigma\ne\tau\), neither \(\mathcal A_\sigma\subseteq
\mathcal A_\tau\) nor the reverse inclusion holds.  An old packet varies a
selected block through all four states of \(\mathcal A_\sigma\).  Relabeling
that selected block by seed \(\tau\) therefore expels two old local owners
and imports two new ones.  The packet owner support is changed.

Thus the hypothesis required by independent packet-state Gram averaging,
namely

\[
 \text{every catalogue state has exactly the same packet owner support}, \tag{7.1}
\]

fails locally.  Deploying all three seeds restores (1.3) only with total
middle multiplicity three.

Even if one temporarily ignores that ownership defect and takes the uniform
fractional average of the three complete seed atlases, the second moment is
not flattened.  Let \(d_\sigma(T)\) be the degree in atlas \(\sigma\), and
put

\[
 d_{\rm frac}(T)={1\over3}\sum_{\sigma=0}^2d_\sigma(T).               \tag{7.2}
\]

All three means are \(\bar d_q\), and their diagonal second moments are
equal by coordinate relabeling.  Since every cross term is nonnegative,

\[
 {1\over N_q}\sum_Td_{\rm frac}(T)^2
 \ge {1\over9}\sum_{\sigma=0}^2
       {1\over N_q}\sum_Td_\sigma(T)^2
 ={1\over3N_q}\sum_Td_0(T)^2.                        \tag{7.3}
\]

Hence three-seed averaging loses at most the constant factor \(3\) from the
exponential in (0.8).  Similarly, context-free independent seed choices
retain a same-seed pair density at least
\(\sum_\sigma p_\sigma^2\ge1/3\).  They cannot remove this mode.  A
possible cure must correlate the seed with the owner context and target
stopping history; independence is insufficient.

### Exact residual lemma \(\mathrm{B4\mbox{-}STOP}\)

An escape from (0.8) requires an integral family of triples

\[
 (\text{owner packet},\ \text{seed field},\ \text{block order})        \tag{7.4}
\]

such that

1. the resulting \(4^r\)-sets partition \(W-o(W)\) physical middle owners;
2. the seed field and order are constant under all \(4^r\) local variations
   of their packet, so first-eligibility is stable;
3. for both signs and every \(q\le H\), the physical stopping degrees obey

\[
 {1\over N_q}\sum_T(d_q(T)-\bar d_q)^2=o(\bar d_q^2/H^2).              \tag{7.5}
\]

Equivalently, it must cancel the positive disjoint-singleton coefficient
represented by the \(\ell=0\) term of (0.5), not merely flatten the
one-target marginal (1.3).

No independent choice among the three relabelled seeds in the already
constructed packets satisfies item 1.  No active-direction permutation
affects item 3.  Therefore \(\mathrm{B4\mbox{-}STOP}\) is a genuinely new
owner-repacketization theorem, rather than a missing probabilistic rounding
step.

## 8. Final conclusion

For the fixed first-eligible \(B_4\) seed, the exact outer collision
coefficient contains the positive negative-binomial term (0.5).  At
\(r\asymp m^{3/4}\) and Gaussian depth it makes the physical Gram excess
exponentially large in \(m^{1/4}\), so the candidate-Gram route cannot give
coefficient one.

The three seed relabelings have identical obstruction coefficients, and
block/direction permutations do not change the complete candidate family.
Context-dependent seed mixing is not ruled out in principle, but it cannot
be performed packetwise on the existing factor: it must first solve the
integral owner-repacketization and stopping-discrepancy lemma
\(\mathrm{B4\mbox{-}STOP}\).  That is the exact coefficient obstruction.
