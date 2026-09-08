# Parity-complete trace factors: the exact two-sign outer occurrence Hall obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, web input, or
independent packet sampling is used.

## 0. Verdict

Grant the local parity-complete mapping construction every requested local
property:

1. the complete-mapping equations are exact;
2. the lifted cycles partition the middle owners exactly;
3. completed direction pairs provide the required Gaussian-scale transport;
4. both signed trace codes are injective at every protected depth; and
5. each packet may choose an arbitrary trace-coded seed, physical
   pair-preserving conjugate, phase, and paired order, with all packet choices
   arbitrarily dependent.

The fixed ordered first-eligible outer packet atlas still cannot cover both
signs with \(o(W)\) holes.  The obstruction is an exact literal-occurrence
Hall cut, not a comparison of raw parity shores.

Let

\[
 W=\binom{2m}{m},\qquad
 q=\lfloor A\sqrt m\rfloor\le\min\{H,r\},
 \qquad A>0\text{ fixed},                          \tag{0.1}
\]

where \(r\to\infty\) and \(r=o(m)\).  Put

\[
 d=A\sqrt{\frac23},
 \qquad
 \boxed{\delta_A=e^{-A^2}\Phi(-d)-\Phi(-2d)>0.}    \tag{0.2}
\]

Then every integral packetwise choice misses

\[
 \boxed{
 M_q^-\ge(\delta_A-o(1))W,
 \qquad
 M_q^+\ge(\delta_A-o(1))W.}                        \tag{0.3}
\]

The coupled two-sign fractional packet LP has uncovered mass

\[
 \boxed{D_q^-+D_q^+\ge(2\delta_A-o(1))W.}          \tag{0.4}
\]

Thus one depth already has a linear deficit.  No correlated packet choice,
dependent rounding, total-unimodularity argument, local trace injection, or
parity-complete paired ordering can produce aggregate \(o(W)\) holes in this
fixed atlas.

The theorem applies both to:

* the raw first-eligible four-block packets \(\mathcal A^r\cong Q_{2r}\);
  and
* the completed common-owner eight-block carrier packets
  \(\mathcal V^r\), partitioned into their \(6^r\) active
  \(Q_{2r}\)-cells.

It does not rule out a moving family of ambient atlases, a component which
physically enters the protected suffix, a cross-packet suffix-fibre splice,
or unrestricted SCI owner recycling.

## 1. The parity shores are routing data, not extra capacity

Write the \(2r\) active cube directions in physical pairs

\[
 (a_i,b_i),\qquad i\in[r],                         \tag{1.1}
\]

and write a packet owner as \((p,x)\in Q_r\times Q_r\), where
\(p_i=a_i\oplus b_i\) and \(x_i=a_i\).  The parity-complete lift alternates
between even and odd \(p\)-contexts.  Its two coarse factors \(G_0,G_1\),
the \(2^{r-1}\) even contexts, and the odd shore are internal successor
routing data for one permutation of the same \(4^r\) owners.

Consequently one trace-coded lifted factor has exactly

\[
 4^r                                             \tag{1.2}
\]

directed phase starts at every signed depth.  It does not have \(2\cdot4^r\)
starts, nor one independent supply for each parity context.  Under the full
trace-code gate, these \(4^r\) starts emit \(4^r\) distinct lower targets and
\(4^r\) distinct upper targets at each protected depth.

Here “full trace-code gate” includes the aligned even-time codes and both
odd-time/odd-length half-step codes.  The aligned code alone does not certify
all phase starts.  In the 24-owner construction we additionally grant
cross-cell physical separation among all \(6^r\) cells; this is a separate
local-tag property, not a consequence of the parity code itself.  If any of
these injectivities fails, the number of distinct targets only decreases, so
the outer obstruction below remains valid.

More generally, let \(\Lambda_r\) be any library of trace-coded triples
\((G_0,G_1,S)\), and let \(g\) be an owner-preserving physical packet
automorphism.  A legal packet state is one whole pair \((\lambda,g)\), and
the fractional normalization is

\[
 \boxed{
 \sum_{(\lambda,g)}x_{P,\lambda,g}=1
 \qquad(P).}                                      \tag{1.3}
\]

Different presentations of the same factor, parity shores, or coarse
factors cannot be counted as additional columns with additional owner mass.

The local existence hypothesis is conditional at growing scale: exact
\(C_{2r}\)-factors of \(Q_r\) require the divisibility \(2r\mid2^r\) (in
the intended recursion, \(r\) is dyadic).  The finite \(r=4\) double-factor
seed by itself is not a Gaussian-scale theorem.  The outer no-go proved here
grants the required growing family nonetheless.

For a completed 24-owner carrier block, choosing one associator shore
partitions the same 24 owners into six four-owner squares.  Tensoring \(r\)
blocks gives \(6^r\) cells but only

\[
 6^r4^r=24^r                                      \tag{1.4}
\]

owners and hence \(24^r\) phase occurrences at one depth.  The six cells
partition capacity; they do not multiply it.  Likewise, the alternative
associator shores are alternative exact resolutions of the same owners, not
simultaneously available occurrence supplies.

Precisely, if \(\mathcal K_\vartheta\) is the set of \(6^r\) disjoint cells
in resolution \(\vartheta\), the whole-packet menu is

\[
 \Theta_P=
 \bigsqcup_{\vartheta}
 \prod_{K\in\mathcal K_\vartheta}\Theta_K.         \tag{1.5}
\]

A packet column chooses one whole resolution and one cell-factor state in
each of its cells.  It is this whole column—not each shore or cell
separately—which receives total packet weight one in (1.3) and (3.2).

## 2. The sharp local paired-face incidence

The local menu itself has a useful exact occurrence census.  It also shows
why a generic all-affine coefficient is not the relevant normalization when
physical pair clustering is retained.

Let

\[
 \Gamma_{\mathrm{pair}}
 =\mathbb F_2^{2r}\rtimes(S_2\wr S_r)              \tag{2.1}
\]

be the cube automorphisms preserving the \(r\) physical direction pairs.
For an affine \(q\)-face, let \(c\) be the number of physical pairs for which
both directions are active, and put

\[
 a=q-2c.                                           \tag{2.2}
\]

Thus \(a\) pairs contribute exactly one active direction.  The number of
affine \(q\)-faces of type \(c\) is

\[
 \boxed{
 N_{r,q,c}
 =2^{2r-q}\binom rc\binom{r-c}{a}2^a,}            \tag{2.3}
\]

with the convention that it is zero unless \(0\le c\le r\) and
\(0\le a\le r-c\).

Indeed, choose the \(c\) completed pairs, the \(a\) split pairs, one of two
directions in every split pair, and the fixed values of the \(2r-q\)
inactive directions.  The group (2.1) is transitive on the faces of each
fixed type \(c\).

### Lemma 2.1 (literal type counts of one paired factor)

Let \(M_{q,c}\) be the number of directed starts whose \(q\)-window spans a
type-\(c\) face.  Under the exact trace-code gate:

* if \(q=2t+1\), then
  \[
  M_{q,t}=4^r,qquad M_{q,c}=0\quad(c\ne t);        \tag{2.4}
  \]
* if \(q=2t\), then
  \[
  M_{q,t}=M_{q,t-1}=\frac{4^r}{2},qquad
  M_{q,c}=0\quad(c\notin\{t-1,t\}).               \tag{2.5}
  \]

#### Proof

The lifted physical direction word consists of adjacent blocks
\((b_i,a_i)\).  An odd window of \(2t+1\) directions contains exactly \(t\)
complete blocks regardless of its boundary parity.  An even window of
\(2t\) directions contains \(t\) complete blocks when aligned with a pair
boundary and \(t-1\) when it begins at the second direction of a pair.
Exactly half the cyclic starts have each boundary parity.  Trace injectivity
makes the selected faces distinct. \(\square\)

Consequently a prescribed type-\(c\) face belongs to the uniformly labelled
pair-preserving menu in the exact fraction

\[
 \boxed{p_{q,c}=\frac{M_{q,c}}{N_{r,q,c}}.}        \tag{2.6}
\]

whenever the assumed trace gate is feasible.  In particular, trace
injectivity forces the orbit-capacity inequalities

\[
 \boxed{M_{q,c}\le N_{r,q,c}\quad\text{for every protected }(q,c).}          \tag{2.7}
\]

These are nonvacuous.  For the finite seed \(r=4,q=4,c=2\), one has
\(M_{4,2}=128\) but \(N_{4,4,2}=96\), so that seed cannot be trace-injective
at every depth.  The conditional theorem below assumes the gate only on the
declared protected range (in the intended regime \(H\ll r\)); the suffix
obstruction itself does not require local injectivity.

Equation (2.6) is the correct local occurrence coefficient.  It does not alter the
outer fact that the sum of all type capacities is exactly \(4^r\) per raw
packet cell and exactly one occurrence per physical middle owner.

## 3. Exact coupled two-sign packet LP

Let \(\mathfrak P\) be either fixed retained packet partition from Section
0, and let \(\Theta_P\) be the allowed menu of whole parity-complete
trace-coded factor states on packet \(P\).  One state \(\theta\) determines
simultaneously every sign and depth.  Let

\[
 A_{P,\theta,q}^{\epsilon}(T)\in\{0,1\}            \tag{3.1}
\]

record whether the state emits target \(T\) at signed depth \((q,\epsilon)\).
This is the binary set-cover support coefficient, whether or not the trace
map is injective.  The trace-code gate additionally says that every support
hit is backed by a unique phase occurrence and that a packet does not lose
capacity to internal repetition.

The all-depth two-sign fractional hole programme is

\[
\begin{aligned}
 \eta:=\min\quad
 &\sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
   \sum_{T\in V_q^\epsilon}z_{q,T}^\epsilon,\\
 z_{q,T}^\epsilon+
 &\sum_{P,\theta}
 A_{P,\theta,q}^{\epsilon}(T)x_{P,\theta}\ge1
 &&(q,\epsilon,T),\\
 &\sum_{\theta\in\Theta_P}x_{P,\theta}=1
 &&(P),\\
 &x_{P,\theta},z_{q,T}^\epsilon\ge0,
\end{aligned}                                      \tag{3.2}
\]

where

\[
 V_q^- =\binom{[2m]}{m-q},
 \qquad
 V_q^+ =\binom{[2m]}{m+q}.                         \tag{3.3}
\]

Its exact dual is

\[
 \boxed{
 \eta=
 \max_{0\le y_{q,T}^\epsilon\le1}
 \left[
  \sum_{q,\epsilon,T}y_{q,T}^\epsilon
  -\sum_{P\in\mathfrak P}
   \max_{\theta\in\Theta_P}
   \sum_{q,\epsilon,T}
    A_{P,\theta,q}^{\epsilon}(T)y_{q,T}^\epsilon
 \right].}                                        \tag{3.4}
\]

The cap \(y\le1\) is supplied by the unit singleton-repair columns.  The
same \(x_{P,\theta}\) occurs at every sign and depth, so (3.2) has not made
separate rankwise choices.

If \(\ell_q^\epsilon(T)\) is the resulting fractional load, define

\[
 D_q^\epsilon
 =\sum_{T\in V_q^\epsilon}(1-\ell_q^\epsilon(T))_+.             \tag{3.5}
\]

For an integral state choice, this is the number of physical holes.  Every
lower bound obtained from (3.4) applies to arbitrary dependence among
integral packet choices as well.

The paired cycles are antipodal after \(2r\) steps, so antipodal starts and
their lower/upper traces form inseparable rounding quartets.  The dual below
gives antipodal partners the same weight within each sign.  It may weight the
two signs differently, but the per-packet maximum evaluates the whole
quartet's combined column weight together.  Thus quartet bundling offers no
escape from the bound.

## 4. A common frozen physical suffix

The two packet models have the same localization property.

### Raw four-block atlas

There are

\[
 b_4=\lfloor m/2\rfloor                            \tag{4.1}
\]

complete four-blocks, and one is eligible with probability \(1/4\) under
independent fair coordinate bits.

### Completed eight-block carrier atlas

There are

\[
 b_8=\lfloor m/4\rfloor                            \tag{4.2}
\]

complete eight-blocks.  Its common-owner carrier has 24 of the 256 local
states, so one block is eligible with probability

\[
 \rho_8=\frac{24}{256}=\frac3{32}.                 \tag{4.3}
\]

In either model, reserve the terminal quarter of complete blocks and let
\(R\) be their union of physical coordinates.  If \(s=|R|\), then

\[
 \frac{s}{2m}\longrightarrow\frac14.              \tag{4.4}
\]

Before \(R\), the expected number of eligible blocks is respectively

\[
 \left(\frac3{32}+o(1)\right)m
 \quad\text{and}\quad
 \left(\frac9{512}+o(1)\right)m.                  \tag{4.5}
\]

Since \(r=o(m)\), Chernoff's inequality gives an absolute
\(c>0\), depending only on the selected model, such that the number
\(U_m\) of middle owners outside the retained cover or in a packet whose
selected list enters \(R\) satisfies

\[
 \boxed{U_m\le e^{-cm}W.}                          \tag{4.6}
\]

Indeed, (4.5) is computed before conditioning, and conditioning independent
fair bits on total rank \(m\) costs only
\(2^{2m}/W=O(\sqrt m)\).  Context stability makes the first-eligible list
constant throughout a retained packet.

For the fixed raw support \(\mathcal A^r\) and for the completed common-owner
support \(\mathcal V^r\), put \(U_{\mathrm{eff}}=U_m\).  If a raw
four-block menu imports owners from the union of all three rank-two
\(B_4\)-supports, write \(U_m^{\mathrm{leave}}\) for the uncovered owner
mass and \(U_m^{\mathrm{bad}}\) for the owner mass in nonnormal canonical
packets, and instead put

\[
 U_{\mathrm{eff}}
 =U_m^{\mathrm{leave}}+\left(\frac32\right)^rU_m^{\mathrm{bad}}.
                                                               \tag{4.6a}
\]

This is still \(e^{-\Omega(m)}W\) because \(r=o(m)\); it follows by comparing
the \(6^r\)-state three-support union with one \(4^r\)-owner raw packet.
The imported menu must obey unit phase-owner incidence on every physical
owner it uses.  For arbitrary local states on the same \(4r\) active
coordinates, the safe multiplier is \(4^r\) in place of \((3/2)^r\), still
exponentially harmless.  No owner-importing menu is charged merely by the
raw \(U_m\).

Call all other packets normal.  Every vertex of every parity-complete factor
state on a normal packet agrees on \(R\).  Hence for every directed phase
owner \(X\), every protected \(q\), and both signs,

\[
 \boxed{
 \tau_{q}^{-}(X)\cap R=X\cap R,
 \qquad
 \tau_{q}^{+}(X)\cap R=X\cap R.}                  \tag{4.7}
\]

This is independent of completed-pair count, direction order, trace code,
associator shore, affine phase, and intrapacket recoupling.  Those operations
move only selected packet coordinates, all lying before \(R\).

## 5. Literal suffix occurrence capacities

For an integer \(z\), define the exact suffix histograms

\[
\begin{aligned}
 B_z&=\left|\left\{X\in\binom{[2m]}m:|X\cap R|=z\right\}\right|,\\
 L_z&=\left|\left\{T\in\binom{[2m]}{m-q}:|T\cap R|=z\right\}\right|,\\
 U_z&=\left|\left\{T\in\binom{[2m]}{m+q}:|T\cap R|=z\right\}\right|.
                                                               \tag{5.1}
\end{aligned}
\]

Thus, exactly,

\[
\begin{aligned}
 B_z&=\binom sz\binom{2m-s}{m-z},\\
 L_z&=\binom sz\binom{2m-s}{m-q-z},\\
 U_z&=\binom sz\binom{2m-s}{m+q-z}.               \tag{5.2}
\end{aligned}
\]

One normal phase owner in suffix class \(z\) supplies exactly one lower and
one upper occurrence in the same suffix class.  Therefore its capacity may
be used once on each sign, but never in another suffix class.

### Proposition 5.1 (exact histogram capacity bound)

For every integral packet state choice,

\[
 \boxed{
 M_q^-+M_q^+
 \ge
 \sum_z\big[(L_z-B_z)_+ +(U_z-B_z)_+\big]-2U_{\mathrm{eff}}.}   \tag{5.3}
\]

For every fractional choice, the same right side is a lower bound on
\(D_q^-+D_q^+\).  Separately,

\[
\begin{aligned}
 M_q^-&\ge\sum_z(L_z-B_z)_+-U_{\mathrm{eff}},\\
 M_q^+&\ge\sum_z(U_z-B_z)_+-U_{\mathrm{eff}},     \tag{5.4}
\end{aligned}
\]

with the analogous fractional statements.

#### Proof

Delete the effective exceptional phase-owner mass \(U_{\mathrm{eff}}\).  In suffix class \(z\),
exact ownership leaves at most \(B_z\) normal phase occurrences.  By (4.7),
their lower target load in that class is at most \(B_z\), and their upper
target load is at most \(B_z\).  Thus the signed uncovered masses are at
least \((L_z-B_z)_+\) and \((U_z-B_z)_+\).  Restore the exceptions.  One
exceptional phase owner can add at most one lower and one upper literal
occurrence, reducing the two-sign deficit by at most two.  This proves
(5.3)--(5.4). \(\square\)

The proposition is a genuine occurrence theorem.  The middle histogram
\(B_z\), not the number of parity shores, associator shores, candidate
frames, or factor presentations, is the available capacity.

There is an equivalent two-tail dual.  For \(a<s/2\), put

\[
\begin{aligned}
 \mathcal Z_{q,a}^-&=
 \left\{T\in V_q^-:|T\cap R|\le a\right\},\\
 \mathcal Z_{q,a}^+&=
 \left\{T\in V_q^+:|T\cap R|\ge s-a\right\},\\
 B_{\le a}&=\sum_{z\le a}B_z.                     \tag{5.5}
\end{aligned}
\]

Put unit dual weight on these two target families and zero elsewhere.  Every
packet state has combined dual occurrence weight at most its number of low
suffix owners plus its number of high suffix owners.  Globally this is at
most \(2B_{\le a}+2U_{\mathrm{eff}}\).  Hence

\[
 \boxed{
 D_q^-+D_q^+
 \ge |\mathcal Z_{q,a}^-|+|\mathcal Z_{q,a}^+|
      -2B_{\le a}-2U_{\mathrm{eff}}.}              \tag{5.6}
\]

Using only one weighted family gives the corresponding separate-sign bound.

## 6. Gaussian evaluation and the sharp explicit constant

Put

\[
 v=\frac3{32},
 \qquad d=A\sqrt{\frac23},
 \qquad
 a_m=\left\lfloor\frac s2-2d\sqrt{vm}\right\rfloor.            \tag{6.1}
\]

Equivalently,

\[
 a_m=\frac s2-\frac A2\sqrt m+O(1).               \tag{6.2}
\]

Stirling's formula, uniformly in the central \(O(\sqrt m)\) range, gives

\[
 \frac{B_{\le a_m}}W\longrightarrow\Phi(-2d),     \tag{6.3}
\]

and

\[
 \frac{|\mathcal Z_{q,a_m}^-|}W
 =\frac{|\mathcal Z_{q,a_m}^+|}W
 \longrightarrow e^{-A^2}\Phi(-d).               \tag{6.4}
\]

Indeed, the suffix count has middle mean \(s/2\), lower mean
\(s/2-(A/4+o(1))\sqrt m\), upper mean
\(s/2+(A/4+o(1))\sqrt m\), and variance
\((v+o(1))m\).  Also

\[
 \frac{\binom{2m}{m-q}}W\longrightarrow e^{-A^2}. \tag{6.5}
\]

The constant in (0.2) is strictly positive.  Writing \(\phi\) for the
standard normal density and using \(A^2=3d^2/2\),

\[
\begin{aligned}
 \delta_A
 &=\int_{-\infty}^{-2d}
   \left[e^{-A^2}\phi(x+d)-\phi(x)\right]dx,\\
 \log\frac{e^{-A^2}\phi(x+d)}{\phi(x)}
 &=-d(x+2d)>0\qquad(x<-2d).                       \tag{6.6}
\end{aligned}
\]

Thus \(\delta_A>0\) for every fixed \(A>0\).  Substituting
(6.3)--(6.4) into (5.6), and using \(U_{\mathrm{eff}}=o(W)\), proves

\[
 D_q^-+D_q^+\ge(2\delta_A-o(1))W.                 \tag{6.7}
\]

The separate one-family duals give

\[
 D_q^-\ge(\delta_A-o(1))W,
 \qquad
 D_q^+\ge(\delta_A-o(1))W.                        \tag{6.8}
\]

Equations (6.7)--(6.8) prove (0.3)--(0.4).  In fact the threshold
\(-2d\) is the unique limiting density crossing, so the same constant is the
positive-part limit in the histogram bound.  This refinement uses the
uniform local hypergeometric CLT on \(O(\sqrt m)\) windows together with
Chernoff domination of the tails:

\[
 \frac1W\sum_z(L_z-B_z)_+\longrightarrow\delta_A,
 \qquad
 \frac1W\sum_z(U_z-B_z)_+\longrightarrow\delta_A. \tag{6.9}
\]

## 7. Why the accepted local parity facts do not evade the cut

1. **Trace-code injectivity.** It prevents two phase starts inside a packet
   from wasting the same labelled target.  It can saturate the available
   suffix-class capacity, but it cannot increase that capacity beyond one
   occurrence per owner.
2. **Completed-pair transport.** It changes local full/empty statistics on
   selected blocks and satisfies the earlier bounded-Lipschitz transport
   test.  It changes no coordinate of \(R\).
3. **Parity-component face matching.** The local SCD face bijection may choose
   a compatible face separately for each target.  A single exact factor must
   realize all those choices with the same one-occurrence-per-owner ledger;
   (5.3) is the missing global constraint.
4. **Associator shores.** The six local cells partition 24 owners, and shore
   rigidity permits one whole shore resolution on a connected owner
   component.  Raw shore cardinalities do not provide extra starts.
5. **Affine trace balance.** Balanced local or abstract face marginals do not
   move mass between different physical suffix fibres.
6. **The audited replicated \(Q_4\) braid bank.** Every component of that
   specific bank remains inside the same early packet support.  Independently,
   when \(q/h\to0\), as in the intended compiler scale \(H\ll h\), its
   entire state cube changes only \(O(qW/h)=o(W)\) occurrences, so it could
   not remove the order-\(W\) dual margin in (6.7).  No such edit-reach claim
   is made for an arbitrary future parity library.

## 8. Constant-one consequence and exact escape boundary

The obstruction occurs at one protected Gaussian depth.  Therefore the
fixed parity-complete packet architecture has aggregate target holes
\(\Omega_A(W)\), and singleton repair alone costs \(\Omega_A(W)\) literal
word positions.

Adding \(o(W/h)\) extra physical \(C_{2h}\)-strips cannot clear the cut.
Each strip supplies only \(2h\) lower and \(2h\) upper occurrences at the
fixed depth, so its total additional two-sign capacity is \(4h\), and the
whole addition supplies only \(o(W)\) occurrences.

A construction can escape this theorem only by invalidating suffix
conservation or the unit owner ledger.  Necessary possibilities are:

1. use a moving family of ambient block orders/supports with no common
   positive-density frozen suffix;
2. build components which physically enter and leave \(R\);
3. splice or trade owners between different suffix fibres; or
4. abandon the exact-factor specialization and prove unrestricted SCI with
   controlled owner recycling.

These are necessary escape categories, not sufficient constructions.  No
claim is made against unrestricted SCI.
