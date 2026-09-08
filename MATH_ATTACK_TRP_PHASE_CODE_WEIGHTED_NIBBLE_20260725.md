# Weighted-overlap nibbling and phase-coded TRP catalogues

Date: 2026-07-25

Pure mathematics only. No fixed-rank matching theorem, computation, solver,
or web input is used.

## 0. Outcome

There are two separate conclusions, one negative and one positive.

First, the tempting ``self-contained weighted-flat nibble theorem'' does
**not** follow from an owner-intersection enumerator alone.  The exact
covariance in a wasteful edge nibble is governed by intersections of
*conflict neighbourhoods*.  If

\[
 \Gamma(e)=\{g:g\cap e\ne\varnothing\},
\]

then its multiplier is

\[
 (1-p)^{-|\Gamma(e)\cap\Gamma(f)|},                  \tag{0.1}
\]

not \(z^{-|e\cap f|}\) as asserted in an earlier draft of this note.
The deterministic comparison

\[
 |\Gamma(e)\cap\Gamma(f)|
 \le (1+o(1))|e\cap f|D+r^2\Delta _2              \tag{0.2}
\]

explains why the following exponentially weighted owner enumerator is the
right *candidate majorant* at residual density \(z\):

\[
 \mathfrak K_z(e)
 =
 \frac1{D_z}
 \sum_{\substack{f:\,\tau(f)\ne\tau(e)}}
 \left[
 z^{-|e\cap f|}
 -1-|e\cap f|(z^{-1}-1)
 \right].                                             \tag{0.3}
\]

Equivalently, if

\[
 \Psi_j(e)
 =\frac1{D_z}
   \sum_{\tau(f)\ne\tau(e)}
       \binom{|e\cap f|}{j},
\]

then the exact binomial identity gives

\[
 \mathfrak K_z(e)
 =\sum_{j=2}^{r}\Psi_j(e)(z^{-1}-1)^j.                \tag{0.4}
\]

But one must also prove that residual degrees and residual pair links stay
flat.  Assuming those dynamic statements, the elementary bite summation
leaves

\[
 O\!\left(
 \eta+
 h\log(1/\eta)+
 r\log(1/\eta)\sup\mathfrak K_z
 \right)W                                             \tag{0.5}
\]

owners, where \(h=o(1/\log(1/\eta))\) is the bite size.  Section 2 proves
the conditional summation lemma and records the exact propagation gate.
It does not claim that (0.3) alone supplies the gate.

Second, ordinary independent catalogue sparsification does not improve
\(\Psi_j\) after degree normalization.  A canonical phase filter does much
better than the short-alphabet code considered in the first draft.

Take, for definiteness,

\[
 \ell=\lfloor m^{3/5}\rfloor,\qquad
 K=\lfloor M/\ell\rfloor,\qquad
 r=\ell+1.                                           \tag{0.6}
\]

Color every middle owner independently and uniformly by the phase set
\([\ell]\).  At every copy tag retain only chunks

\[
 P=(X_0,\ldots,X_{\ell-1})
\]

with the canonical schedule

\[
 \operatorname{col}(X_t)=t
 \quad(0\le t<\ell).                                  \tag{0.7}
\]

The expected tag and owner degrees are both multiplied by \(\ell^{-\ell}\);
their original ratio is unchanged. The residual scalar degree remains
enormous:

\[
 \log(D_L\ell^{-\ell})
 =(3/2+o(1))\ell\log m-\ell\log\ell
 =(9/10+o(1))\ell\log m.                             \tag{0.8}
\]

The exact timed rotor identity gives the uniform conditional expected
ledger

\[
 \delta_{\rm phase}=(1+o(1))\frac\ell{m^2},
 \qquad
 r^2\delta_{\rm phase}
 =O(\ell^3/m^2)=O(m^{-1/5}).                         \tag{0.9}
\]

Most importantly, a shared owner has one global phase color, so it must
occur at the **same phase** in both retained chunks.  Every nonzero-shift
subchunk, and every intersection using varying phase offsets, is removed
identically.

This is a genuine improvement, but it does not yet prove the exact
conflict-neighbourhood hierarchy. The
remaining enemy is a large *scattered phase-aligned* intersection.  Hence
the canonical catalogue passes the expected degree, pair-codegree, and
shifted-subchunk tests, but concentration for one coloring and the full
dynamic weighted hierarchy remain open.

## 1. The exact covariance object

Regard a tag as an ordinary vertex.  Thus every catalogue edge consists of
one tag and \(r-1\) distinct owners.  Edges sharing a tag conflict
automatically.

In a current residual hypergraph \(G\), write \(D\) for the reference
degree, \(\Delta _2\) for the maximum pair degree, and

\[
 \Gamma(A)=\{g\in G:g\cap A\ne\varnothing\}.          \tag{1.1}
\]

Mark every edge independently with probability

\[
 p=\frac{h}{rD}.                                      \tag{1.2}
\]

Delete every vertex touched by a marked edge and retain precisely the
isolated marked edges.  If \(I_e\) is the event that no marked edge meets
\(e\), then the two exact identities are

\[
 \Pr(I_e=1)=(1-p)^{|\Gamma(e)|},                      \tag{1.3}
\]

\[
 \frac{\Pr(I_e=I_f=1)}{\Pr(I_e=1)\Pr(I_f=1)}
 =(1-p)^{-|\Gamma(e)\cap\Gamma(f)|}.                 \tag{1.4}
\]

Equation (1.4), not an independent-owner formula, is the source of the
exponential weight.

There is a useful deterministic reduction to edge intersections.  Assign
to every \(g\in\Gamma(e)\cap\Gamma(f)\) one pair
\((x,y)\in(e\cap g)\times(f\cap g)\).  Union bounding over the assigned
pairs gives

\[
 \begin{aligned}
 |\Gamma(e)\cap\Gamma(f)|
 &\le \sum_{x\in e}\sum_{y\in f}d(x,y)\\
 &\le (1+\epsilon)|e\cap f|D+r^2\Delta _2,           \tag{1.5}
 \end{aligned}
\]

where \(d(x,x)=d(x)\) and all current degrees are at most
\((1+\epsilon)D\).  If \(\Delta _2\le\delta D\), (1.4)--(1.5) imply

\[
 (1-p)^{-|\Gamma(e)\cap\Gamma(f)|}
 \le
 \exp\left\{(1+o(1))\frac{h}{r}|e\cap f|
              +O(hr\delta)\right\}.                 \tag{1.6}
\]

Over \(\Theta((r/h)\log(1/z))\) bites, the first exponent accumulates to
\(z^{-O(|e\cap f|)}\), while the second remains harmless only if

\[
 r^2\delta\log(1/\eta)=o(1).                         \tag{1.7}
\]

This proves the origin and the necessary scale of the weighted hierarchy.
It does not prove that residual degrees or residual links obey it.

## 2. What a self-contained nibble theorem may honestly assert

### Lemma 2.1 (conditional bite summation)

Suppose a wasteful nibble admits a trajectory down to owner density
\(\eta\) such that, at every bite:

1. all but an \(\epsilon\)-fraction of current vertices have degree
   \((1\pm\epsilon)D_t\);
2. the bite removes a \((1+O(h+\epsilon))h/r\) fraction of current
   nonexceptional owners; and
3. collision-wasted owners and owners discarded to restore the trajectory
   conditions total at most

   \[
    C\frac hr(h+\epsilon+\kappa)|R_t|.                \tag{2.1}
   \]

If

\[
 (h+\epsilon+\kappa)\log(1/\eta)=o(1),               \tag{2.2}
\]

then the retained isolated edges form a matching with owner leave

\[
 \boxed{
 L_O\le
 C\left[\eta+(h+\epsilon+\kappa)\log(1/\eta)\right]
 |\mathcal O|.}                                      \tag{2.3}
\]

If the initial tag capacity equals \(|\mathcal O|/(r-1)+o(|\mathcal
O|/r)\), its tag leave is

\[
 L_T\le\frac{L_O+o(|\mathcal O|)}{r-1}.              \tag{2.4}
\]

#### Proof

The population decreases geometrically by a factor
\(1-(1+o(1))h/r\), so at most

\[
 T\le(1+o(1))\frac rh\log(1/\eta)                    \tag{2.5}
\]

bites are needed.  Summing (2.1) along this trajectory gives at most

\[
 C(h+\epsilon+\kappa)\log(1/\eta)|\mathcal O|        \tag{2.6}
\]

wasted owners.  Add the final \(\eta|\mathcal O|\) owners.  If \(s\)
edges were retained, then

\[
 L_O=|\mathcal O|-(r-1)s,
 \qquad L_T=|\mathcal T|-s,                          \tag{2.7}
\]

which proves both conclusions. \(\square\)

Conditions 2--3 have the correct one-bite scale.  Indeed, (1.3), degree
flatness, and a union bound give collision probability \(O(h)\) for a
marked edge and hence \(O(h^2/r)\) owner waste in one bite.  The hard step
is keeping condition 1 and the pair-link analogue valid for all the bites.

### The exact propagation gate

A sufficient dynamic gate is the following pair of requirements in every
current residual, uniformly for every edge \(e\):

\[
 r^2\frac{\Delta _2}{D}\log(1/\eta)=o(1),            \tag{2.8}
\]

\[
 \sum_{j\ge2}\Psi_j(e)(c/z)^j
 =o\left(\frac1{r\log(1/\eta)}\right),               \tag{2.9}
\]

where \(z\) is the current owner density and \(c>1\) absorbs the harmless
constants in (1.6).  Equations (1.4)--(1.6) then make every covariance
remainder summable.  The qualifier **dynamic** is essential: a bound for
the initial catalogue does not itself show that the same bound holds after
conditioning on earlier bites.

Thus Lemma 2.1 is a completely proved summation theorem, while
(2.8)--(2.9) are the still-unproved TRP propagation gate.  The earlier
draft's formula

\[
 \mathbb E I_eI_f=\mathbb EI_e\,\mathbb EI_f\,
 z^{-|e\cap f|}
\]

was false for the wasteful nibble and must not be used.

## 3. Independent sparsification does not help

Retain every catalogue edge independently with probability \(q\). For a
fixed retained edge \(e\), let \(D'\) and \(\Psi'_j(e)\) be the thinned
degree and normalized overlap moments. Then

\[
 \mathbb ED'=qD,                                      \tag{3.1}
\]

\[
 \mathbb E\left[
 \sum_{f\ne e}\binom{|e\cap f|}{j}
 \,\middle|\,e\text{ retained}\right]
 =qD\Psi_j(e).                                        \tag{3.2}
\]

Consequently

\[
 \mathbb E\Psi'_j(e)=\Psi_j(e)+o(1)                   \tag{3.3}
\]

whenever the thinned degree concentrates. The same cancellation holds for
any independent thinning whose retention weights are asymptotically
constant on every relevant link.  Arbitrary nonuniform weights can change
\(\Psi_j\), but only by being deliberately correlated with the overlap
geometry; that is a structured phase restriction, not catalogue-blind
sparsification.

Thus independent subcatalogue sampling reduces absolute degree and
codegree together but does not improve the weighted hierarchy. A useful
sparsification must correlate retention with phase or overlap.

## 4. The canonical phase catalogue

Choose

\[
 \ell=\lfloor m^{3/5}\rfloor,
 \qquad K=\lfloor M/\ell\rfloor,
 \qquad r=\ell+1.                                    \tag{4.1}
\]

The calibrated rotor parameters satisfy

\[
 Q\ll\ell\ll m^{2/3},                                \tag{4.2}
\]

which is the useful interval for this construction.  Independently color
every middle owner uniformly from \([\ell]=\{0,\ldots,\ell-1\}\).  At
every tag \((U,c)\), retain a repetition-free chunk

\[
 P=(X_0,\ldots,X_{\ell-1})
\]

exactly when

\[
 \operatorname{col}(X_t)=t
 \qquad(0\le t<\ell).                                \tag{4.3}
\]

The schedule is identical for all copy labels.  This distinction from a
distinct color for every *copy-phase* is crucial.

Let \(d_1\) be the uncolored degree of one prescribed timed owner
condition, summed over its containing carriers but for one copy label.
For owners \(X,Y\) at Johnson distance \(\delta\), let \(d_2(s;X,Y)\) be
the corresponding degree with \(X\) and \(Y\) prescribed at two phases at
lag \(s\).  In the unpruned stationary catalogue the exact timed rotor
identity is

\[
 \boxed{
 \frac{d_2(s;X,Y)}{d_1}
 =\frac{\pi_s(\delta)}{\binom m\delta^2}.}             \tag{4.4}
\]

Removing the \(e^{-\Omega(Q)}\) fraction of owner-repeating chunks changes
both sides of every ledger below by a uniform \(1+o(1)\) factor.  Thus
(4.4) is used exactly before pruning and asymptotically after pruning.

For \(s\le Q\), \(\pi_s(\delta)=\mathbf1_{\{\delta=s\}}\); for
\(s>Q\), \(\pi_s(1)=e^{-\Omega(Q)}\).

### Proposition 4.1 (exact expected degree and pair ledger)

Before fixing the owner coloring,

\[
 \mathbb E D_L^{\rm ph}=\ell^{-\ell}D_L,
 \qquad
 \mathbb E D_R^{\rm ph}=\ell^{-\ell}D_R.             \tag{4.5}
\]

Condition on the colors of two distinct owners and average over all other
owner colors.  Their normalized codegree is at most

\[
 \boxed{
 \delta_{\rm ph}
 \le(1+o(1))\frac\ell{m^2}.}                          \tag{4.6}
\]

Consequently

\[
 r^2\delta_{\rm ph}
 =O(\ell^3/m^2)=O(m^{-1/5})=o(1).                    \tag{4.7}
\]

#### Proof

A simple chunk has \(\ell\) distinct owners, so (4.3) has probability
\(\ell^{-\ell}\), proving the tag statement.

Fix an owner \(X\) of color \(t\).  It can occur only at phase \(t\), but
it can occur in each of the \(K\) copy labels.  The other \(\ell-1\)
owners cost \(\ell^{-(\ell-1)}\), so

\[
 \mathbb E d^{\rm ph}(X)
 =K d_1\ell^{-(\ell-1)}
 =\ell^{-\ell}(K\ell d_1)
 =\ell^{-\ell}D_R.                                   \tag{4.8}
\]

Now let \(X,Y\) have colors \(t,u\).  If \(t=u\), no simple chunk can
contain them both at their allowed phase.  If \(s=|u-t|>0\), then

\[
 \frac{\mathbb E d^{\rm ph}(X,Y)}
      {\mathbb E d^{\rm ph}(X)}
 =\ell\frac{d_2(s;X,Y)}{d_1}
 =\ell\frac{\pi_s(\delta)}{\binom m\delta^2}.         \tag{4.9}
\]

For \(\delta=1\), the maximum occurs at \(s=1\) and equals
\(\ell/m^2\); later lags have the factor \(e^{-\Omega(Q)}\).  For
\(\delta\ge2\), (4.9) is \(O(\ell/m^4)\).  This proves (4.6).
A tag--owner codegree has normalized size at most \(\ell/B\), which is
negligible, and two tag vertices have codegree zero. \(\square\)

Finally the expected scalar degree is still enormous:

\[
 \begin{aligned}
 \log(D_L\ell^{-\ell})
 &=(3/2+o(1))\ell\log m-\ell\log\ell\\
 &=(9/10+o(1))\ell\log m.                            \tag{4.10}
 \end{aligned}
\]

## 5. Exact removal of shifted subchunks

### Corollary 5.1 (phase alignment)

If two retained chunks share an owner \(X\), then \(X\) occurs at the same
phase in both chunks.

#### Proof

If \(X\) occurs at phases \(t,u\), (4.3) gives
\(\operatorname{col}(X)=t=u\). \(\square\)

Thus every nonzero-shift common run is impossible, not merely rare or
short.  A common set of owners is indexed by one common phase set
\(S\subseteq[\ell]\).  This removes both adjacent shifted windows and
scattered intersections using varying phase offsets.

The remaining aligned runs have a direct chronology estimate.

### Lemma 5.2 (specified owner-trajectory bound)

Fix a carrier \(U\), an initial owner \(X_0\), and a valid prescribed
sequence of consecutive owners

\[
 X_0,X_1,\ldots,X_{k-1}.
\]

For a stationary uniform rotor chunk in \(U\),

\[
 \boxed{
 \Pr(X(\omega_t)=X_t\text{ for }0\le t<k
       \mid X(\omega_0)=X_0)
 \le[(m-Q)(H-Q)]^{-(k-1)}.}                           \tag{5.1}
\]

#### Proof

Put \(a=m-Q\), \(b=H-Q\). The owner transition identifies its entrant
\(y_t=X_{t+1}-X_t\) and departure
\(z_{Q,t}=X_t-X_{t+1}\).

For the first \(q=\min(Q,k-1)\) transitions, the prescribed departures fix
\(q\) ordered entries of the initial owner queue. Conditional on \(X_0\),
these entries are a uniform injective \(q\)-tuple from \(X_0\), costing
\((m)_q^{-1}\). Every prescribed entrant costs \(b^{-1}\).

After \(Q\) transitions, the departure at time \(t+Q\) is the earlier
choice \(x_t\). Hence \(k-Q-1\) of the \(x\)-choices are also prescribed
when \(k>Q+1\), each costing \(a^{-1}\). Therefore the probability is at
most

\[
 (m)_q^{-1}b^{-(k-1)}
 a^{-\max(0,k-Q-1)}.                                  \tag{5.2}
\]

If \(k\le Q+1\), then \((m)_{k-1}\ge a^{k-1}\). If
\(k>Q+1\), then \((m)_Q\ge a^Q\). In both cases (5.2) is at most
\((ab)^{-(k-1)}\), proving (5.1). \(\square\)

Conditioning on one retained chunk can save at most \(k\) of the phase
color constraints for a second chunk sharing an aligned run of length
\(k\).  The worst normalized gain is therefore \(\ell^k\), and the run
series has geometric ratio

\[
 \frac{\ell}{(m-Q)(H-Q)}=m^{-9/10+o(1)}.              \tag{5.3}
\]

Hence every single aligned consecutive-run contribution is exponentially
summable.

## 6. The remaining aligned hierarchy

The maximum pair codegree (4.6) is attained only by an owner pair whose
colors are adjacent phases and whose Johnson distance is one.  Along one
fixed rotor chunk those exceptional pairs are sparse.  This gives a
sharper edgewise second-overlap ledger than the maximum-codegree bound.

### Proposition 6.1 (edgewise second overlap)

For every retained chunk \(P\), in expectation over the remaining owner
colors,

\[
 \boxed{\Psi^{\rm ph}_2(P)=O(\ell^2/m^2).}             \tag{6.1}
\]

#### Proof

Sum (4.9) over the \(\binom\ell2\) phase pairs of \(P\).  At lag
\(1\le s\le Q\), rotor geodesicity gives Johnson distance exactly \(s\).
The \(s=1\) terms contribute \(O(\ell^2/m^2)\), while all
\(2\le s\le Q\) terms together contribute \(O(Q\ell^2/m^4)\).

For \(s>Q\), a distance-one pair has the factor \(e^{-\Omega(Q)}\), and a
pair at distance at least two has denominator at least \(\binom m2^2\).
All late lags therefore contribute

\[
 O(\ell^3e^{-\Omega(Q)}/m^2+\ell^3/m^4),
\]

which is smaller than the lag-one term. \(\square\)

In particular, with \(\eta=1/\log m\), the entire \(j=2\) part of the
weighted gate has the required scale:

\[
 (\log m)^2\Psi^{\rm ph}_2(P)
 =o\left(\frac1{\ell\log\log m}\right),              \tag{6.2}
\]

because \(\ell^3(\log m)^2\log\log m/m^2=o(1)\).

What remains is the aligned higher-overlap statement

\[
 \boxed{
 \max_P\sum_{j=3}^{\ell}
 \Psi_j^{\rm ph}(P)(c\log m)^j
 =o\left(\frac1{\ell\log\log m}\right).}             \tag{6.3}
\]

Lemma 5.2 proves (6.3) for phase sets forming one consecutive run.  It does
not prove it for many separated aligned runs: conditioning on two
geodesic endpoints can put a prescribed intermediate owner on a constant
fraction of their link.  A proof must charge each new run either to a
fresh carrier-union expansion or to a late return of probability
\(e^{-\Omega(Q)}\).  That multi-run charging theorem, and its propagation
through residual bites, are still open.

## 7. Audit of the other restrictions

Uniform independent edge thinning fails by (3.1)--(3.3).

A one-start marker, with mark probability \(1/\ell\), exactly balances tag,
marked-start-owner, and unmarked-internal-owner degrees in expectation.  It
kills an adjacent suffix/prefix shift but not a common run internal in both
chunks.

Giving every *copy-phase* a distinct color uses \(K\ell\asymp m\) colors.
The timed identity then gives relative lag-one codegree

\[
 (K\ell)/m^2=(1+o(1))/m,
\]

so \(r^2\delta\asymp\ell^2/m\), which diverges for every
reset-compatible \(\ell\gg Q\).  The failure comes from encoding the copy
label.  The canonical phase filter deliberately does not encode it.

A shorter random phase alphabet can cap every shifted common run while
preserving the pair ledger, but it still permits scattered intersections
at varying equal-symbol phases.  The canonical \(\ell\)-phase schedule is
strictly cleaner: it removes every phase misalignment and passes the basic
ledger precisely in the range \(Q\ll\ell\ll m^{2/3}\).

## 8. Coefficient-one ledger

The phase restriction does not alter path chronology. With
\(\ell=m^{3/5}\),

\[
 O(QW/\ell)=o(W)                                      \tag{8.1}
\]

for resets, and

\[
 O(\ell W/m)=o(W)                                     \tag{8.2}
\]

for carrier remainders.

If the higher aligned estimate (6.3), its residual propagation, and
canonical-degree concentration are proved, Lemma 2.1 with
\(\eta=1/\log m\) yields

\[
 L_O=o(W),\qquad L_T=o(W/\ell),                       \tag{8.3}
\]

and the owner-only compiled length is \(W+o(W)\).

No simultaneous flag conclusion follows: phase coding addresses owner
overlaps only.

## 9. Final status

### Proved

1. The exact conflict-neighbourhood covariance identity (1.4), its
   reduction (1.5), and the conditional bite-summation lemma (2.3).
2. Independent thinning preserves normalized overlap moments and is
useless against shifted chunks.
3. The canonical phase filter forces every common owner to the same phase,
   so every shifted subchunk is absent.
4. Exact expected degree scaling \(\ell^{-\ell}\), with residual scalar
   degree \(\exp\{(9/10+o(1))\ell\log m\}\).
5. The uniform conditional expected pair ledger
   \(\delta_{\rm ph}=O(\ell/m^2)\), hence
   \(r^2\delta_{\rm ph}=o(1)\).
6. The stronger edgewise identity
   \(\Psi^{\rm ph}_2(P)=O(\ell^2/m^2)\), which closes the \(j=2\)
   weighted gate.
7. The specified rotor trajectory probability is at most
   \([(m-Q)(H-Q)]^{-(k-1)}\).
8. Every single aligned consecutive-run series is exponentially summable.
9. Scalar degree, reset, and remainder ledgers remain favorable.

### Open

1. Concentration of all canonical degrees for one fixed owner coloring.
2. The separated aligned higher-overlap hierarchy (6.3).
3. Propagation of that hierarchy through all residual bites.
4. Therefore the canonical-phase owner near-factor.
5. Flag-compatible selection.

The canonical phase filter removes the exact shifted-subchunk obstruction
without destroying the expected degree or pair ledgers. The remaining
problem is narrower: factorially suppress scattered *phase-aligned*
coincidences of two rotor chunks and propagate that suppression through the
nibble.
