# Global PBBS slack, critical arithmetic, and protected component packaging

Date: 2026-07-31.

Status: exact arithmetic dichotomy, exact protected-fragment formulation,
a constructive reset--Hall sufficient theorem, and an exact Catalan
two-rail endpoint-complement specialization.  This note does **not** claim
the all-\(k\) upper bound: the protected router, upper cut kernel, and final
common-cap compiler remain simultaneous existence gates.

## 0. Verdict

There are three different ledgers which must not be conflated.

1. The canonical PBBS factor has a controlled number of components.
2. A component opening must recycle its deleted lower-\(q_1\) colour and
   preserve an upper witness.
3. The resulting chronology has an exact, position-sensitive deadline loss.

The first ledger is now arithmetically sharp.  Away from the last member of
a constant-depth plateau, the scalar slack is larger than the entire
Catalan number, so it dominates the crude PBBS component count.  The
previously observed stronger assertion

\[
                    s(2m+1)>\frac13\operatorname{Cat}_m
\tag{0.1}
\]

except at \(m=4\) is false: exact counterexamples occur at

\[
 (m,d_m)=(225669,421),\qquad (691583,737).
\tag{0.2}
\]

Both are terminal plateau dimensions and both have positive slack strictly
below \(\operatorname{Cat}_m/3\).  Such exceptional plateau indices have
density zero, but neither finiteness nor infinitude follows from the present
number theory.

The second and third ledgers admit an exact theorem.  Relative to a complete
occurrence-labelled fragment catalogue, protected packaging is precisely a
coloured directed-path system with cut-kernel, upper-crossing, and exact
staircase constraints.  In the one-path/one-boundary-port case, **every**
new seam must be Johnson and the seam colours must be exactly all but one of
the deleted colours.  A forward rectangular reset--colour Hall condition is
a concrete all-dimensional sufficient hypothesis: it gives one protected
rainbow path with staircase loss zero.  This is the correct global
component lemma to prove for PBBS.  A comparison such as \(c_m-1\le s_m\)
does not imply it.

For the odd lift there is now a stricter alternative.  Exact lower coverage
forces \(2\operatorname{Cat}_m\) cross seams and two
\(\operatorname{Cat}_m\)-path rail forests.  Their complete lower palette is
equivalent to one endpoint-complement equation plus containment matching
and one-cycle monodromy.  This is the literal Catalan braid ledger in
Section 8.  It can have zero staircase charge even when its seam count is
larger than scalar slack, but it still needs protected upper witnesses and
one common cap.

## 1. Odd deadline arithmetic

Put

\[
 C_m=\operatorname{Cat}_m,qquad
 W_m={2m+1\choose m}=(2m+1)C_m,qquad
 L_m=4^m-1,
\tag{1.1}
\]

and write

\[
 Q_d={d+1\choose2},\qquad
 S_m(d)=dW_m+Q_d-L_m.
\tag{1.2}
\]

The deadline depth and its scalar slack are

\[
 d_m=\min\{d:S_m(d)\ge0\},\qquad s_m=S_m(d_m).
\tag{1.3}
\]

For \(k=2m+1\), these are exactly \(d(k)\) and
\(\operatorname{slack}(k)\), because the complete strict-lower mass is
\(4^m-1\).

### Lemma 1.1 (exact Catalan and slack recurrences)

For every \(m,d\ge1\),

\[
 C_{m+1}=\frac{2(2m+1)}{m+2}C_m,
 \qquad
 W_{m+1}=4W_m-C_{m+1},
\tag{1.4}
\]

and

\[
 \boxed{S_{m+1}(d)=4S_m(d)-dC_{m+1}-3(Q_d+1).}
\tag{1.5}
\]

Moreover \(d_m\) is nondecreasing and

\[
                         d_{m+1}-d_m\in\{0,1\}.
\tag{1.6}
\]

#### Proof

The two binomial identities in (1.4) are immediate.  Substituting them and
\(L_{m+1}=4L_m+3\) in (1.2) gives (1.5).

If \(S_m(d)<0\), then (1.5) gives \(S_{m+1}(d)<0\), proving monotonicity.
For the upper increment, first note that \(d_m\le m\) for \(m\ge2\): the
quantity \(mW_m/4^m\) is at least its value at \(m=2\) and increases under
(1.4).  If \(S_m(d)\ge0\), then direct subtraction gives

\[
 S_{m+1}(d+1)
 =4S_m(d)+\left(4-\frac{2(d+1)}{m+2}\right)W_m
   -3Q_d+d-2.
\tag{1.7}
\]

For \(d\le m\) the coefficient of \(W_m\) is greater than two, while
\(W_m\ge m(m+1)\); hence the last two terms together are nonnegative.
The cases \(m=1,2\) are direct.  Thus \(d+1\) is feasible at \(m+1\),
proving (1.6). \(\square\)

Call \(m\) **noncritical** when \(d_{m+1}=d_m\), and **critical** when
\(d_{m+1}=d_m+1\).  Thus a critical \(m\) is the last member of a depth
plateau.

### Theorem 1.2 (noncritical slack dominates the Catalan component bank)

If \(m\) is noncritical and \(d=d_m\), then

\[
 s_m\ge
 \frac d4 C_{m+1}+\frac34(Q_d+1)
 =\frac{d(2m+1)}{2(m+2)}C_m+\frac34(Q_d+1).
\tag{1.8}
\]

Consequently \(s_m>C_m/2\) always, and, whenever \(d_m\ge2\),

\[
                              \boxed{s_m>C_m.}
\tag{1.9}
\]

In particular the crude PBBS component bill \(c_m-1\le C_m-1\) fits the
scalar slack at every noncritical odd dimension with \(d_m\ge2\).

#### Proof

Noncriticality says \(S_{m+1}(d)=s_{m+1}\ge0\).  Rearranging (1.5) proves
(1.8).  For \(m,d\ge1\),

\[
 \frac{d(2m+1)}{2(m+2)}\ge\frac12.
\]

If \(d\ge2\), the same ratio is at least one.  The positive final term in
(1.8) makes both comparisons strict. \(\square\)

The last sentence is only a scalar screen.  Sections 4--7 prove why it is
not a component-opening theorem.

### Corollary 1.3 (all one-third failures are critical)

If \(s_m\le C_m/3\), then \(m\) is critical.

#### Proof

Theorem 1.2 is already stronger.  Equivalently, (1.5) and
\(C_{m+1}/C_m>2\) give \(S_{m+1}(d_m)<0\), while Lemma 1.1 then forces the
depth to increase by one. \(\square\)

## 2. Critical roots and the false one-third law

Define

\[
                         \rho_m=\frac{4^m}{W_m}.
\tag{2.1}
\]

The recurrence in (1.4) gives

\[
                  \rho_{m+1}=\rho_m\frac{2m+4}{2m+3}.
\tag{2.2}
\]

### Lemma 2.1 (a sharp Wallis window)

For every \(m\ge1\),

\[
 \boxed{
 \frac\pi4\left(m+\frac54\right)
 <\rho_m^2<
 \frac\pi4\left(m+\frac54+\frac1{16m}\right).}
\tag{2.3}
\]

#### Proof

Put

\[
 u_m=\frac4\pi\rho_m^2-m-\frac54.
\]

Equation (2.2) gives

\[
 u_{m+1}=\left(\frac{2m+4}{2m+3}\right)^2u_m
           -\frac1{4(2m+3)^2}.
\tag{2.4}
\]

Backward iteration, using the standard Wallis estimate \(u_m=O(1)\), gives

\[
 u_m=\sum_{j=m}^{\infty}
 \frac1{4(2j+3)^2}
 \prod_{i=m}^{j}\left(\frac{2i+3}{2i+4}\right)^2.
\tag{2.5}
\]

The first summand and the sum with all products dropped give

\[
 \frac1{16(m+2)^2}<u_m<
 \sum_{j=m}^{\infty}\frac1{4(2j+3)^2}
 <\frac1{16}\sum_{n=m+1}^{\infty}\frac1{n^2}
 <\frac1{16m}
\]

and hence (2.3). \(\square\)

The rational enclosure

\[
              \frac{103993}{33102}<\pi<\frac{104348}{33215}
\tag{2.6}
\]

is certified, for example, by the alternating series in Machin's formula
\(\pi=16\arctan(1/5)-4\arctan(1/239)\).

### Theorem 2.2 (two exact positive-slack counterexamples)

The one-third law (0.1) fails at each pair in (0.2).  More precisely,

\[
 \begin{array}{c|c|c|c}
 m&2m+1&d_m&s_m/C_m\\ \hline
 225669&451339&421&0.0624199861\ldots\\
 691583&1383167&737&0.2020913679\ldots
 \end{array}
\tag{2.7}
\]

and in both rows

\[
                         0<s_m<C_m/3.
\tag{2.8}
\]

#### Proof

For the first row, (2.3), (2.6), and exact rational cross multiplication
give

\[
 \frac{103993}{4\cdot33102}\left(m+\frac54\right)
 -\left(421-\frac1{4(451339)}\right)^2
 =\frac{34225828436843}{107889689111535072}>0,
\tag{2.9}
\]

and

\[
 421^2-
 \frac{104348}{4\cdot33215}
 \left(m+\frac54+\frac1{16m}\right)
 =\frac{11708701}{119929533360}>0.
\tag{2.10}
\]

Hence

\[
                421-\frac1{4(451339)}<\rho_m<421.
\tag{2.11}
\]

Since \(Q_{421}=88831\), the upper inequality makes depth 421 feasible.
For depth 420, (2.11) gives

\[
 W_m(\rho_m-420)>W_m\left(1-\frac1{4(451339)}\right)
                       >Q_{420}+1,
\]

so depth 420 is infeasible.  Moreover

\[
 \frac{s_m}{C_m}
 =(2m+1)(421-\rho_m)+\frac{Q_{421}+1}{C_m}
 <\frac14+\frac1{12}<\frac13,
\tag{2.12}
\]

where \(C_m\ge C_{14}=2674440>12\cdot88832\).  Positivity follows from
\(\rho_m<421\).

For the second row the exact comparisons are

\[
 \frac{103993}{4\cdot33102}\left(m+\frac54\right)
 -\left(737-\frac3{10(1383167)}\right)^2
 =\frac{111150655755673}{25331649097290271200}>0,
\tag{2.13}
\]

and

\[
 737^2-
 \frac{104348}{4\cdot33215}
 \left(m+\frac54+\frac1{16m}\right)
 =\frac{11613377}{73506973904}>0.
\tag{2.14}
\]

Thus \(737-3/[10(1383167)]<\rho_m<737\).  Now
\(Q_{737}=271953\) and
\(C_m\ge C_{15}=9694845>30\cdot271954\), so

\[
 \frac{s_m}{C_m}<\frac3{10}+\frac1{30}=\frac13.
\]

The same feasibility argument proves \(d_m=737\): depth 737 is feasible,
whereas

\[
 W_m(\rho_m-736)>W_m\left(1-\frac3{10(1383167)}\right)
                       >Q_{736}+1
\]

rules out depth 736. \(\square\)

Both examples are critical by Corollary 1.3.  They arise from the restricted
upper approximants

\[
 \frac{16\cdot421^2}{4\cdot225669+5}
 =\frac{2835856}{902681},\qquad
 \frac{16\cdot737^2}{4\cdot691583+5}
 =\frac{8690704}{2766337}
\tag{2.15}
\]

to \(\pi\).

### Theorem 2.3 (critical dimensions are sparse; bad critical depths have density zero)

One has

\[
 d_m=\frac{\sqrt{\pi m}}2+O(1).
\tag{2.16}
\]

Hence only \(O(\sqrt M)\) values \(m\le M\) are critical.  If \(M_d\)
is the terminal member of the depth-\(d\) plateau, then, for all
sufficiently large \(d\),

\[
 M_d\in\left\{
 \left\lfloor\frac{4d^2}{\pi}-\frac54\right\rfloor-1,
 \left\lfloor\frac{4d^2}{\pi}-\frac54\right\rfloor
 \right\}.
\tag{2.17}
\]

In the second case, putting
\(\theta_d=\{4d^2/\pi-5/4\}\), one has

\[
 \frac{s_{M_d}}{C_{M_d}}=d\theta_d+O(d^{-1}).
\tag{2.18}
\]

In the first case the same left side is
\(d(1+\theta_d)+O(d^{-1})\), and hence exceeds \(1/3\) for all sufficiently
large \(d\).

In particular, depths for which \(s_{M_d}\le C_{M_d}/3\) have natural
density zero.

#### Proof

Equation (2.3) gives \(\rho_m=\sqrt{\pi m}/2+O(m^{-1/2})\), while
(1.3) differs from the threshold \(d\ge\rho_m\) by
\((Q_d+1)/W_m=o(1)\).  This proves (2.16), and Lemma 1.1 then counts the
critical values.

Solving the squared Wallis window (2.3) for its crossing with \(d^2\)
puts the real crossing at
\(4d^2/\pi-5/4+O(d^{-2})\), which gives (2.17).  If
necessary, the positive lower bound
\(u_m>1/[16(m+2)^2]\) rules out feasibility at the integer above
\(\lfloor4d^2/\pi-5/4\rfloor\): the deadline correction
\((Q_d+1)/W_m\) is exponentially smaller.  If

\[
 \theta_d=\left\{4d^2/\pi-5/4\right\},
\]

then, in the second case, subtracting \(\rho_{M_d}^2\) from \(d^2\),
dividing by \(d+\rho_{M_d}\), and using
\(2M_d+1=8d^2/\pi+O(1)\) gives (2.18).  If the Wallis correction moves the
terminal integer down by one, the same calculation replaces \(\theta_d\)
by \(1+\theta_d\).  The exponentially small
\((Q_d+1)/C_{M_d}\) is absorbed in the error.

The sequence \(\{4d^2/\pi-5/4\}\) is equidistributed by Weyl's polynomial
equidistribution theorem.  By (2.18), failure implies
\(\theta_d\le1/(3d)+O(d^{-2})\).  For every fixed \(\varepsilon>0\), all
sufficiently large failures therefore lie in \([0,\varepsilon]\), whose
equidistribution density is \(\varepsilon\).  Letting
\(\varepsilon\downarrow0\) proves density zero. \(\square\)

Density zero is not finiteness.  Proving infinitely or finitely many
solutions of this shrinking-target condition is a separate Diophantine
problem and is unnecessary for the protected reset theorem below.

## 3. PBBS component census versus scalar slack

Let \(c_m\) be the number of cycles of the canonical PBBS permutation and
let \(a_m\) count cycles of the minimum physical period \(2m+1\).  The
normalized cycle lengths \(\ell_i\) are positive odd integers and

\[
                         \sum_i\ell_i=C_m.
\tag{3.1}
\]

Therefore

\[
 C_m\ge a_m+3(c_m-a_m)
\tag{3.2}
\]

and

\[
 \boxed{
 c_m-a_m\le\left\lfloor\frac{C_m-a_m}{3}\right\rfloor,
 \qquad
 c_m\le\left\lfloor\frac{C_m+2a_m}{3}\right\rfloor.}
\tag{3.3}
\]

This factor-three theorem has two exact consequences.

* At every noncritical dimension with \(d_m\ge2\), Theorem 1.2 already
  gives \(c_m-1<s_m\), without using (3.3).
* At a critical dimension, (3.3) alone certifies \(c_m-1\le s_m\) provided

  \[
                         C_m+2a_m\le3s_m+5.
  \tag{3.4}
  \]

The constant five in (3.4) is the exact integer floor: it is equivalent to
\(\lfloor(C_m+2a_m)/3\rfloor\le s_m+1\).  At either counterexample in
Theorem 2.2 the right side of the equivalent bound

\[
                 a_m\le\left\lfloor\frac{3s_m-C_m+5}{2}\right\rfloor
\tag{3.5}
\]

is negative.  Thus the factor-three theorem cannot certify even the raw
seam bill there.  This does **not** prove that the actual \(c_m\) exceeds
\(s_m+1\).

If minimum-period components have zero charged halo mass, only the
nonminimum count is charged and (3.2) gives a strict \(C_m/3\) bound.  The
zero-charge assertion is a combinatorial reset property, not a consequence
of their period.

### Corollary 3.1 (Catalan-gap component neutrality)

At an odd-to-odd Pascal step, suppose the untagged target palette has size
\(M=N+C\), the auxiliary old shore has \(N\) owners, and the Catalan macro
bank has \(C\) cyclic gaps.  If the old shore is cut into \(c\le C\)
nonempty paths and these paths are inserted into \(c\) distinct gaps, then
the cyclic untagged slot count is exactly

\[
                         (N-c)+2c+(C-c)=M.
\tag{3.6}
\]

If \(c\le C-1\), opening one retained direct gap gives exactly \(M-1\)
linear slots.  More generally one may open any certified seam whose deletion
leaves one spanning path.  Thus
the component number is neutral at the **unlabelled slot** level.  Since the
PBBS bound gives \(c_m\le C_m\), there are enough cyclic Catalan gaps
whenever the relevant PBBS path cover is the auxiliary shore; a retained
direct opening additionally needs \(c_m<C_m\) or a separately certified
port opening.

This corollary proves neither endpoint containment nor colour injectivity.
The internal, two-port, and retained-direct colours must jointly form the
required palette, and the pure-old upper targets must retain internal
witnesses.  Those are exactly the labelled conditions in Sections 4--7.

## 4. Exact lower-\(q_1\) seam conservation

Let a lower-\(q_1\)-exact cyclic Johnson factor on \(W\) middle owners be
cut at \(b\) distinct edges, at least one in every component.  It becomes
\(b\) nonempty oriented fragments.  Let \(R\) be the \(b\)-set of deleted
colours.  Join the fragments by a directed seam forest with \(p\) path
components.  Suppose \(n\) selected seams are non-Johnson, so the number of
Johnson seams is

\[
                              A=b-p-n.
\tag{4.1}
\]

Let \(Q\) be the multiset of their intersection colours and \(m_Q(C)\) its
multiplicity.  If \(\mu(C)\) is the final adjacency multiplicity, then

\[
                         \boxed{
 \mu(C)=1-\mathbf1_R(C)+m_Q(C).}
\tag{4.2}
\]

Let \(H\) be the number of missing lower-\(q_1\) colours and \(E\) the
total multiplicity excess.  Then

\[
 \begin{aligned}
 H&=\#\{r\in R:m_Q(r)=0\},\\
 E&=\sum_{r\in R}(m_Q(r)-1)_+
    +\sum_{C\notin R}m_Q(C),
 \end{aligned}
\tag{4.3}
\]

and exactly

\[
                         \boxed{H-E=p+n,\qquad H=p+n+E.}
\tag{4.4}
\]

#### Proof

Only cut edges and new seams alter the original exact palette, proving
(4.2)--(4.3).  The final number of valid Johnson colour occurrences is

\[
                    (W-b)+A=W-p-n.
\]

Comparing this with \(W-H+E\) gives (4.4). \(\square\)

For one final path and one boundary/compiler port, exact lower-\(q_1\)
completion is possible precisely when

\[
                  n=0,\qquad E=0,\qquad Q=R\setminus\{\rho\}
\tag{4.5}
\]

for one deleted colour \(\rho\) which the boundary port can realize.  Thus
all \(b-1\) seams must be Johnson and must recycle distinct deleted colours.
The often-used identity \(H-E=b-j\) is correct only when \(j=A\) denotes
the number of Johnson seams; if \(j\) denotes final path components, the
correct identity is (4.4).

## 5. Protected cuts and exact cross-fragment upper witnesses

On an original component \(K_i\), retain every cyclic interval occurrence
witnessing an upper target \(Z\).  Let \(\mathcal W_i(Z)\) be this occurrence
family and let \(E(I)\) be the set of component edges crossed by occurrence
\(I\).

With one cut edge \(e_i\), define

\[
                         B_i(Z)=\bigcap_{I\in\mathcal W_i(Z)}E(I).
\tag{5.1}
\]

Then \(Z\) retains an internal witness on \(K_i\) exactly when

\[
                              e_i\notin B_i(Z).
\tag{5.2}
\]

With several cuts \(K_i^{\rm cut}\), the exact condition is

\[
 \exists I\in\mathcal W_i(Z)\quad
                  E(I)\cap K_i^{\rm cut}=\varnothing.
\tag{5.3}
\]

Checking the cuts separately is insufficient: collectively they can hit
every witness span even when no individual cut belongs to (5.1).

For a fixed final fragment order \(\pi\), every new crossing interval has
the unique form

\[
 \text{suffix(first fragment)}\ \cup\
 \text{all intervening fragments}\ \cup\
 \text{prefix(last fragment)}.
\tag{5.4}
\]

Thus upper completeness is exactly the union of the internal bank from
(5.3) and the literal crossing bank from (5.4).  This is the protected
cut-kernel interface; mere component connectivity has no upper implication.

## 6. Exact protected packaging theorem

Fix one cut set, the resulting fragmentation, and one orientation of every
fragment.  Let the occurrence-labelled seam catalogue contain every legal
directed seam for this fixed data.  A seam record includes its endpoint
occurrences, Johnson/non-Johnson status, colour when Johnson, run-state
transition, and the suffix/prefix data needed for (5.4).

For a selected spanning-path arc set \(x\), let \(T_x\) be its unique
concatenated middle chronology.  Let \(\Psi_d(T_x)\) denote the exact
minimum scalar staircase loss over all nondecreasing start-threshold vectors \(G\), with
the coordinatewise-minimal deadline vector \(H^G\), subject to row
exactness and chain alignment.  If no such schedule exists, set
\(\Psi_d(T_x)=+\infty\).  This is the arbitrary-start optimizer from the
deadline-staircase theorem; it does not include common-cap feasibility.

### Theorem 6.1 (fixed-fragmentation protected packaging: exact finite system)

Relative to the fixed fragmentation and exhaustive seam catalogue, a
protected packaging into one spanning path with scalar loss at most \(s\)
exists if and only if one can choose binary seam variables \(x_a\)
satisfying all four groups below.

**P1. One directed spanning path.**

\[
 \deg_x^+(F)\le1,qquad \deg_x^-(F)\le1,qquad
 \sum_a x_a=b-1,
\tag{6.1}
\]

and, for every nonempty fragment set \(X\),

\[
       \sum_{a:\,\operatorname{tail}(a),\operatorname{head}(a)\in X}x_a
       \le |X|-1.
\tag{6.2}
\]

**P2. Literal lower-\(q_1\) restoration.**  For some \(\rho\in R\), every
selected seam is Johnson, the selected colour multiset is exactly
\(R\setminus\{\rho\}\), and \(\rho\) is assigned to an actually compatible
boundary/compiler port.  Equivalently, (4.5) holds.

**P3. All-depth upper preservation.**  Every upper target belongs either
to the internal bank (5.3) or to the crossing bank (5.4) of the selected
order.

**P4. Exact staircase acceptance.**

\[
                              \Psi_d(T_x)\le s.
\tag{6.3}
\]

If the resulting pinned lower atlas has an integral common-cap assignment,
these conditions produce a literal contiguous-OR word of length \(W+d\).
With the independent lower
bound, this proves \(\nu(k)=B(k)\).

#### Proof

The degree, cardinality, and subtour constraints are exactly one spanning
directed path.  Equation (4.2) is the complete change in the lower-\(q_1\)
palette, proving P2.  Every interval after cutting and
reordering is either internal to one fragment or has the form (5.4), so P3
is exact.  The arbitrary-start staircase theorem makes P4 equivalent to a
row-exact, chain-aligned schedule of loss at most \(s\).  These implications
are reversible relative to the fixed fragmentation and exhaustive seam
catalogue.  If cuts or orientations are also variable, this theorem applies
inside each consistent outer choice; a union catalogue additionally needs
explicit exact-one and owner-partition constraints.

Finally, the common-cap assignment realizes every strict-lower target in
the same physical letters while preserving the middle staircase.  P3 and
chain alignment transfer every upper witness to a physical interval.
Hence the resulting word is universal. \(\square\)

Theorem 6.1 is not advertised as an efficient generic algorithm.  Its value
is logical: it identifies the exact finite object, and it proves that no
scalar component estimate can replace P2--P4 or the common cap.

## 7. A constructive all-dimensional reset--Hall lemma

There is a strong local hypothesis under which P1--P4 become genuinely
constructive.  Cut once in each of \(b\) components and fix one orientation
of every fragment.  Fix initial fragment \(\alpha\), terminal fragment
\(\omega\), omitted cut colour \(\rho\), and put
\(R'=R\setminus\{\rho\}\).

Assume first that every upper target has an internal witness surviving the
chosen cuts.  The same statement allows seam-served vulnerable targets if
the required suffix--prefix service bundle is included in every product
rectangle below.

For every \(q\in R'\), let \(O_q\) be a set of allowed tail fragments and
\(I_q\) a set of allowed head fragments.  Assume:

\[
 O_q\subseteq\mathcal F\setminus\{\omega\},\qquad
 I_q\subseteq\mathcal F\setminus\{\alpha\}.
\tag{7.0}
\]

1. \(O_q\cap I_q=\varnothing\), and every pair in the full rectangle
   \(O_q\times I_q\) is a literal protected Johnson seam of colour \(q\);
2. one common strict potential \(h\) satisfies \(h(F)<h(G)\) for every
   pair \((F,G)\in O_q\times I_q\);
3. every fragment has at least \(d+1\) owners and no internal positive
   coordinate run of length at most \(d\), while every positive run which
   is bounded inside a two-fragment product concatenation and meets its seam
   has length at least \(d+1\);
4. the two Hall systems hold:

   \[
   \left|\{q\in R':O_q\cap X\ne\varnothing\}\right|\ge|X|
   \quad(X\subseteq\mathcal F\setminus\{\omega\}),
   \tag{7.1}
   \]

   \[
   \left|\bigcup_{q\in Y}I_q\right|\ge|Y|
   \quad(Y\subseteq R').
   \tag{7.2}
   \]

Here the first Hall matching assigns every nonterminal tail a distinct
colour, and the second assigns those same colours to distinct noninitial
heads.

### Theorem 7.1 (forward rectangular reset--colour Hall)

Under assumptions 1--4, the two Hall matchings compose by colour into one
Hamilton fragment path from \(\alpha\) to \(\omega\).  It uses exactly the
colours \(R'\), preserves the protected upper bank, and has

\[
                             \Psi_d(T)=0.
\tag{7.3}
\]

Consequently, if the \(\rho\)-boundary port and the integral common cap are
feasible, then \(\nu(k)=B(k)\).

#### Proof

Hall (7.1) bijects the \(b-1\) nonterminal tails with \(R'\); Hall (7.2)
bijects \(R'\) with the \(b-1\) noninitial heads.  Rectangular closure makes
every composed pair a legal seam.  Thus every fragment except \(\omega\)
has outdegree one and every fragment except \(\alpha\) has indegree one.
The common strict potential excludes directed cycles, so the cover is one
Hamilton path.  Its colour set is exactly \(R'\), and (4.5) proves the
palette assertion.

Any short positive run in the final chronology is either internal to one
fragment, closes across one seam, or crosses at least two seams.  The first
two cases are excluded by assumption 3.  In the third case the run contains
an entire intervening fragment, of length at least \(d+1\), so it is not
short.  The flat staircase is therefore row-exact and has loss zero.  Upper
protection and the final compiler implication are Theorem 6.1. \(\square\)

This theorem is a concrete PBBS target, not a property currently known for
the canonical factor.  The full guarded-Hall version, allowing a charged
initial halo of length \(M\le s(k)\), is proved in
`MATH_THEOREM_K_PROTECTED_RAINBOW_RESET_FRAGMENT_PACKING_20260731.md`.

## 8. Catalan two-rail endpoint-complement specialization

The protected component problem has a much sharper odd-lift specialization.
Let \(m\ge2\), let \(\Omega=[2m]\), add \(z\), and put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\tag{8.1}
\]

The child middle layer is the disjoint union of the \(N\) unmarked
rank-\((m+1)\) states and the \(M\) marked copies
\(z+\binom\Omega m\).

### Theorem 8.1 (forced Catalan crossing count)

Every spanning Johnson degree-two child factor which covers the complete
lower-\(q_1\) palette has exactly

\[
 \boxed{
 e_{UU}=N-K,\qquad e_{CC}=N,\qquad e_{UC}=2K,}
\tag{8.2}
\]

and every lower colour occurs once.

#### Proof

If the cross count is \(2R\), degree sums give
\(e_{UU}=N-R\) and \(e_{CC}=M-R\).  The \(N\) tagged colours can only come
from marked internal edges, so \(R\le K\).  The \(M\) untagged colours come
from unmarked internal and cross edges, so
\(N-R+2R\ge M\), or \(R\ge K\).  Hence \(R=K\).  The total edge and palette
counts are both \(M+N\), so coverage is exact. \(\square\)

Thus a connected/Hamilton zero-defect object is intrinsically a pair of
Catalan path forests, not a collection of arbitrary PBBS component seams.

### Theorem 8.2 (endpoint-complement braid)

Suppose the marked rail is partitioned into \(K\) nontrivial paths whose
\(N\) internal intersection colours enumerate
\(\binom\Omega{m-1}\).  Suppose the unmarked rail is partitioned into
\(K\) paths whose \(N-K\) internal intersection colours form a set
\(L\subseteq\binom\Omega m\).  Assume the \(2K\) marked endpoint labels are
distinct and equal

\[
                       \binom\Omega m\setminus L.
\tag{8.3}
\]

Any perfect containment matching from the marked endpoint occurrences
\(C\) to the unmarked endpoint occurrences \(U\), with \(C\subset U\),
produces a degree-two factor with the complete lower palette exactly once.
It is one Hamilton cycle precisely when its contracted two-regular
bipartite fragment graph is one alternating cycle.  Conversely, every
lower-rainbow factor in this two-rail forest fibre has exactly this form.

#### Proof

The marked internal bank gives all tagged colours, the unmarked internal
bank gives \(L\), and every cross seam has lower colour equal to its marked
endpoint.  Equation (8.3) therefore supplies the complementary untagged
bank exactly.  Endpoint matching restores degree two.  Contraction preserves
connected components.  The converse follows from Theorem 8.1 and the same
three disjoint palette banks. \(\square\)

Opening one cross seam of colour \(\rho\) gives one spanning path missing
only \(\rho\), provided the contracted graph was connected.  The colour
\(\rho\) must have a literal boundary/compiler port.

The proposed duplicate-cut ledger is the following exact corollary.  Start
from rail 2-factors, let the unmarked intersections be injective with unused
facet set \(\mathcal E\), and suppose the marked intersections have profile
\(1^{N-K}2^K\).  Cut one edge from every doubled marked class and cut \(K\)
unmarked edges, hitting every source cycle so that each deleted rail is a
union of exactly \(K\) paths.  If \(D_C,D_U\) are the cut banks, exact lower
coverage is equivalent to the endpoint/facet equation

\[
 \boxed{
       \partial D_C
       =\mathcal E\mathbin{\dot\cup}\lambda_U(D_U)}
\tag{8.4}
\]

together with the displayed path-forest condition, containment Hall, and
one-cycle monodromy.  The right side of (8.4) is a set, so the marked cuts
must form a matching.  The floor profile alone does not imply (8.4).  The
weaker and more general hypothesis is only that the retained marked forest
has the exact tagged palette.

The hosted cap-two switch gives a small sufficient subfamily of (8.4).  For
each unused facet \(X\) inserted in a host block, retain one incident edge
\(XR_X\), cut the other \(XJ_X\), and cut the unmarked edge of colour
\(J_X\).  For a fixed host injection the retained-colour and distinct-
\(J_X\) requirements form an exact 2-SAT instance.  This hosted-square
subfamily is not a normalization of all endpoint-complement braids.

The lower theorem plugs into Theorem 6.1 only with the remaining protected
conditions:

1. every target avoiding \(z\) has a witness wholly inside one retained
   unmarked fragment;
2. every target containing \(z\) has an internal marked witness or a
   literal suffix--whole-fragments--prefix witness in the final order;
3. the opened chronology is chain aligned and has
   \(\Psi_{d_m}\le s_m\);
4. the boundary colour \(\rho\) has a compatible port; and
5. the pinned lower atlas has one integral common cap.

Under these conditions Theorem 6.1 gives
\(\nu(2m+1)=B(2m+1)\).  If every fragment and every allowed two-fragment
product is reset-clean, then \(\Psi_d=0\): the \(2K\) physical seams are
palette-neutral and collectively have zero staircase charge.  Hence this
architecture bypasses, rather than pays, the Catalan component bill and is
not blocked by the slack-zero or slack-below-\(K/3\) dimensions in Section
2.

The authenticated finite anatomy is sharp.  At \(k=15\),

\[
 (M,N,K)=(3432,3003,429),\qquad
 (e_{UU},e_{CC},e_{UC})=(2574,3003,858).
\tag{8.5}
\]

For every choice of \(z\), the resident all-depth-complete two-cycle factor
has exactly these counts, satisfies the endpoint-complement palette and
containment conditions, and has \(429\) paths on each rail.  Its contracted
cycle type is \((426)(3)\), so it misses one-cycle monodromy.  Moreover its
hosted-square compatibility graph has eleven isolated cross seams for every
\(z\); it is a rigorous non-instance of the narrow local switch while being
a positive calibration of the broader theorem.

For the \(k=16\) carrier viewed as a possible \(k=17\) source,

\[
 (M,N,K)=(12870,11440,1430),\qquad
 (e_{UU},e_{CC},e_{UC})=(10010,11440,2860).
\tag{8.6}
\]

The authenticated endpoint-reroot path is not the required cap-two marked
rail: its rank-nine union loads are
\(1^{10111}2^{1229}3^{100}\), and its endpoints are not Johnson-adjacent.
A one-edge closure cannot remove the triple loads.  This closes only that
fixed K16 source, not existence of another cap-two package.

The full theorem and audit are
`MATH_THEOREM_K_CATALAN_TWO_RAIL_ENDPOINT_COMPLEMENT_BRAID_20260731.md`
and `MATH_AUDIT_K_CATALAN_TWO_RAIL_K15_K16_ANATOMY_20260731.md`.

## 9. Why seam count cannot bound staircase loss

Even after topology and palette are fixed, staircase loss is positional.
For \(d=1\), suppose one coordinate trace has exactly one internal positive
singleton run, beginning at zero-based owner index \(a\),
\(1\le a\le W-2\), and no other coordinate imposes a stronger condition.
Then the exact arbitrary-start optimizer is

\[
                         \boxed{\Psi_1(T)=\min(a,W-a-1).}
\tag{9.1}
\]

Indeed, with the single start/deadline thresholds \(G,H\), residence of the
singleton requires either \(G\le a+1\) or \(H\ge a\).  In the first case
the loss is at least \(W-a-1\), attained by \((G,H)=(a+1,0)\); in the
second it is at least \(a\), attained by \((G,H)=(W,a)\).

Thus one locally legal seam near \(W/2\) can create deadline loss of order
\(W\).  The comparison \(c-1\le s\) contains no information about
\(\Psi_d\).  This is an abstract scheduling obstruction; it is not asserted
to occur in the canonical PBBS factor without a literal trace construction.

Other independent failures are equally elementary:

* extra protected cuts can make the fragment count \(b\) exceed \(c\);
* a seam graph can spend \(b-1\) arcs in a directed subtour and isolate a
  fragment;
* a Hamilton scaffold can use distinct colours outside \(R\), producing
  \(H=b\) and \(E=b-1\) rather than recycling the cut bank;
* several individually harmless cuts can collectively hit every upper
  witness; and
* marginal Hall does not imply one nonempty common cap.

## 10. Exact remaining theorem

The arithmetic and component census reduce the all-odd PBBS lane to the
following occurrence-level statement.

> **Protected PBBS reset router.**  For every \(m\), choose protected cuts
> and orientations so that the deleted-colour bank admits a rainbow acyclic
> seam set \(R\setminus\{\rho\}\), every upper target has an internal or
> seam-crossing witness, and the resulting run product satisfies
> \(\Psi_{d_m}\le s_m\).  In addition, the \(\rho\)-port and the strict-lower
> common-cap system must be jointly feasible.

Theorem 7.1 proves this from the stronger forward rectangular reset--Hall
hypothesis.  The charged-halo theorem in the companion note proves it from
fully guarded source-colour Hall plus an initial ideal of mass at most
\(s_m\).

Section 8 supplies a second, sharper sufficient route for an odd lift:
construct the protected Catalan endpoint-complement braid.  It replaces the
deleted-colour router by two \(K\)-path forests, equation (8.3), containment
Hall, and one-cycle monodromy.  Under a reset-clean product its \(2K\) seams
have \(\Psi_d=0\), so this route does not require \(2K\le s_m\).  The two
routes share the all-depth cut kernel, boundary port, and common-cap gates;
neither is presently proved for all \(m\).

At noncritical dimensions there is ample scalar capacity, but P2--P3 and
the common cap are still real.  At critical dimensions, including the two
counterexamples above, a zero-loss/reset-clean router or a direct actual
component/halo census is indispensable.  Since bad critical depths have
density zero, they may be treated by a separate architecture, but an
asymptotic-density argument cannot prove the exact statement
\(\nu(k)=B(k)\) for every \(k\).

The first exceptional critical point is \(m=4\) (\(k=9\)), where
\(s_m=0\); the known optimum therefore belongs to the zero-loss/separate-
architecture branch.  Theorem 2.2 proves that this is not the only
dimension at which the one-third scalar shortcut fails.

For even dimensions one must additionally prove that the odd-to-even
Pascal/facet braid preserves this protected router and its common cap.  No
even conclusion follows merely from the odd PBBS component count.

## 11. Audit and artifact scope

The independent proof audit is
`MATH_AUDIT_K_GLOBAL_PBBS_SLACK_AND_PROTECTED_RESET_PACKING_20260731.md`.
The constructive guarded-Hall/charged-halo theorem used in Section 7 is
`MATH_THEOREM_K_PROTECTED_RAINBOW_RESET_FRAGMENT_PACKING_20260731.md`.
The two-rail specialization and its finite replay are
`MATH_THEOREM_K_CATALAN_TWO_RAIL_ENDPOINT_COMPLEMENT_BRAID_20260731.md`
and `MATH_AUDIT_K_CATALAN_TWO_RAIL_K15_K16_ANATOMY_20260731.md`.

The exact arithmetic replayers are

```text
scratch/audit_global_pbbs_slack_component_20260731.py
scratch/global_pbbs_slack_component_20260731.audit.json
scratch/global_pbbs_slack_component_20260731.bigint.audit.json
```

The default replay proves the Machin rational enclosure, both Wallis
certificates, and the complete small table through \(m=20\).  The optional
`--bigint` replay also reconstructs the two large Catalan and slack integers
and checks their frozen unsigned-big-endian hashes.  Neither replay searches
Boolean factors or supplies the missing protected PBBS router.
