# Boundary OR-deck compression and the fixed-4 connector census

Date: 2026-07-31  
Lane: A, coverage-level upper compression  
Status: exact linear/cyclic coverage theorem and fixed-4 physical connector
construction proved; contracted ECO and retained-detour calibrations audited;
residence and common-baseline quadratic supply remain separate

## 0. Verdict

For existential contiguous-OR coverage, pointwise prefix/suffix equality is
stronger than necessary.  Let

* every old prefix-union value occur among the new prefixes;
* every old suffix-union value occur among the new suffixes;
* the old and new total unions agree; and
* every old internal interval-union value occur internally in the new block.

Then replacement preserves every old interval-OR target in every fixed linear
exterior.  These are four unary deck tests; no occurrence address is exported.

This weaker interface materially improves the fixed-4 C6 geometry.  Among
the \(48\) serializations of each matching phase, exactly \(24\) ordered
old/new pairs are deck-transparent, and exactly \(6\) of those are literal
Johnson paths in both phases.  One canonical pair is

\[
\begin{aligned}
 X={}&(H+ab,H+az,H+bz,H+bc,H+cz,H+ac),\\
 Y={}&(H+ab,H+bz,H+bc,H+cz,H+az,H+ac).
\end{aligned}                                                     \tag{0.1}
\]

Thus the antipodal-seam obstruction of the pointwise-signature serialization
is removed at the coverage level.

The gain is structured, not automatic.

* In the contracted twelve-owner all-six ECO bank, \(25\) common connector
  matchings are literal Johnson matchings, \(6\) Hamiltonize both phases,
  and exactly \(3\) of those pass the complete boundary-deck plus
  internal-dominance test, with \(12\) cut/orientation pairs in total.
* In the explicit fourteen-owner retained-detour calibration, none of the
  \(28^2=784\) old/new cut-orientation pairs passes, even under the compressed
  criterion.

Boundary residence, run lengths, occurrence ownership, multiplicity and
common-cap state are not preserved by deck inclusion and remain separate.

## 1. Boundary decks

For \(X=(X_1,\ldots,X_h)\), write

\[
\begin{aligned}
 {\cal P}(X)&=\left\{\bigcup_{i=1}^jX_i:1\le j\le h\right\},\\
 {\cal S}(X)&=\left\{\bigcup_{i=j}^hX_i:1\le j\le h\right\},\\
 {\cal D}(X)&=\left\{\bigcup_{i=s}^tX_i:1\le s\le t\le h\right\},\\
 T(X)&=\bigcup_{i=1}^hX_i .
\end{aligned}                                                     \tag{1.1}
\]

These are sets of distinct OR values, not ordered chains or multisets.

### Theorem 1.1 (compressed linear replacement)

Let \(W=LXS\) and \(W'=LYS\), with \(X,Y\) occupying the same slot.  Assume

\[
\begin{aligned}
 {\cal P}(X)&\subseteq{\cal P}(Y),&
 {\cal S}(X)&\subseteq{\cal S}(Y),\\
 T(X)&=T(Y),&
 {\cal D}(X)&\subseteq{\cal D}(Y).
\end{aligned}                                                     \tag{1.2}
\]

Then every interval-union value covered by \(W\) is covered by \(W'\).

#### Proof

An old interval disjoint from the slot is unchanged.  If it crosses only
the left boundary, its value is an unchanged suffix union of \(L\) united
with one member \(P\in{\cal P}(X)\).  Choose a new prefix with union \(P\).
The right-boundary case is identical with \({\cal S}\).  An interval
crossing both boundaries contains the whole slot and uses \(T(X)=T(Y)\).
Finally, an interval internal to \(X\) has a value in \({\cal D}(X)\), hence
in \({\cal D}(Y)\). \(\square\)

Equal slot lengths are not needed for target coverage alone, but are retained
in packet applications because owner count, addresses, residence and the
common-cap schedule depend on length.

### Theorem 1.2 (many disjoint slots)

Suppose pairwise disjoint fixed slots \(X_1,\ldots,X_t\) are replaced by
\(Y_1,\ldots,Y_t\), each satisfying (1.2).  Then every old interval-union
target remains covered.

#### Proof

Intervals meeting zero or one replaced slot are covered by Theorem 1.1,
including the case crossing both boundaries of that one slot.  If an
interval meets at least two slots, its first and last met slots contribute
respectively either a suffix-deck value or their total, and either a
prefix-deck value or their total; every strictly intermediate slot
contributes its total union.  Choose the matching new suffix and prefix
endpoints independently.  This constructs one new interval with the same
union. \(\square\)

This direct proof is preferable to a sequential address argument because
deck witnesses may move inside their slots.

## 2. Cyclic scope

If full-cycle intervals are admitted, Theorem 1.1 also holds for one fixed
proper slot in a cyclic word.  The only new case is an old proper cyclic
interval containing the entire exterior and meeting the slot in a separated
prefix \(P_i(X)\) and suffix \(S_j(X)\), with \(i+1<j\).  Choose indices
\(p,q\) in \(Y\) with

\[
                    P_p(Y)=P_i(X),\qquad S_q(Y)=S_j(X).           \tag{2.1}
\]

If \(p+1<q\), the corresponding proper wrap interval in the new cycle has
the same value.  If \(p+1\ge q\), the selected prefix and suffix cover all of
\(Y\), so

\[
 P_i(X)\cup S_j(X)=P_p(Y)\cup S_q(Y)=T(Y)=T(X).                 \tag{2.2}
\]

The old interval value is therefore the OR of the full cycle, and the
admissible full-cycle interval realizes it after replacement.

If full-cycle intervals are excluded, separate prefix and suffix decks are
not sufficient in the overlap-or-abut case.  Put
\(P_0(X)=S_{h+1}(X)=\varnothing\).  One must additionally preserve the
proper two-ended deck

\[
 {\cal J}^{\circ}(X)=
 \{P_i(X)\cup S_j(X):0\le i\le h,\ 1\le j\le h+1,\ i+1<j\}.    \tag{2.3}
\]

The strict inequality records a nonempty omitted gap.  The correct
context-independent hypothesis for every proper cyclic exterior is
\({\cal J}^{\circ}(X)\subseteq{\cal J}^{\circ}(Y)\); allowing merely
disjoint but abutting pieces is insufficient because they cover the whole
slot.

The strictness is necessary.  With exterior cell \(\{e\}\), take

\[
 X=(\{a,b\},\{b\},\{c\}),\qquad
 Y=(\{a\},\{b\},\{c\}).                                      \tag{2.4}
\]

The four linear deck conditions (1.2) hold, and even the weak two-ended deck
allowing abutting pieces is contained.  But the old proper wrap interval
\((\{c\},\{e\},\{a,b\})\) has value \(\{a,b,c,e\}\), whereas in the new
cycle that value occurs only on the forbidden full cycle.  The separated
deck catches this: \(\{a,b,c\}\in{\cal J}^{\circ}(X)\) but
\(\{a,b,c\}\notin{\cal J}^{\circ}(Y)\).

For the final linear contiguous-OR word, Theorems 1.1--1.2 are the relevant
form and no cyclic convention is needed.

## 3. What the compressed criterion does not preserve

Deck inclusion does not preserve:

* the address or length of a witness;
* multiplicity of one target;
* width/depth grading;
* first/last coordinate occurrence times;
* positive-run or zero-run lengths at a boundary;
* occurrence-labelled owner/compiler assignments.

Thus residence must retain its clipped prefix/suffix run state and every
forbidden internal short run as a separate unary row.  A width-graded
compiler must use graded deck inclusion or its own exact matching ledger.

For composition across several slots, “retain” means equality, for every
coordinate (and for both bit polarities when gaps are constrained), of the
clipped leading run, clipped trailing run and whole-fragment flag, together
with internal short-run safety.  Checking each replacement only against the
old exterior is not compositional; adjacent slots must instead export these
equal boundary states or be certified jointly in one halo row.

As in the internal-dominance theorem, these deck rows are unary legality
checks.  If their combined failure graph has an \(O(d)\) vertex cover, they
delete only \(O(md)\) parameter pairs and add no semantic witness tickets
to row energy.

## 4. A literal all-Johnson fixed-4 packet

Suppress the common core \(H\).  In (0.1), every consecutive pair in both
\(X\) and \(Y\) shares exactly one of the four active coordinates, so both
are Johnson paths.  Their matching edges in positions \(12,34,56\) are the
two phases of the fixed-4 incidence C6:

\[
\begin{aligned}
 E^-&=\{ab\!-\!az,\ bz\!-\!bc,\ cz\!-\!ac\},\\
 E^+&=\{ab\!-\!bz,\ bc\!-\!cz,\ az\!-\!ac\}.
\end{aligned}                                                     \tag{4.1}
\]

The two words use the same six middle owners and have the same first owner
\(H+ab\) and last owner \(H+ac\).  Consequently replacement inside a fixed
exterior preserves both boundary adjacencies and the occurrence-labelled
degree-two path/cycle topology literally.  The same conclusion holds in the
unlabelled owner graph when these six owners are private to the slot, as in
an exact middle-owner factor.  Without privacy, a repeated exterior owner
can change simple-owner degree.  Also, the two inter-edge seams do change,
so this is a path rethread, not by itself a common-connector alternating
switch.

### Theorem 4.1 (fixed-4 deck transparency)

The words (0.1) satisfy (1.2) in both directions.  Explicitly,

\[
 {\cal P}(X)={\cal P}(Y)=\{H+ab,H+abz,H+abcz\},                   \tag{4.2}
\]

\[
 {\cal S}(X)={\cal S}(Y)=\{H+ac,H+acz,H+abcz\},                   \tag{4.3}
\]

and

\[
\begin{split}
 {\cal D}(X)={\cal D}(Y)
   ={}&\{H+ab,H+az,H+bz,H+bc,H+cz,H+ac,\\
      &H+abz,H+bcz,H+acz,H+abcz\}.
\end{split}                                                       \tag{4.4}
\]

#### Proof

Take consecutive unions directly.  The prefix chains have values

\[
 (ab,abz,abz,abcz,abcz,abcz)
\quad\hbox{and}\quad
 (ab,abz,abcz,abcz,abcz,abcz),
\]

whose distinct-value sets agree.  The suffix chains similarly have common
distinct-value set \(\{ac,acz,abcz\}\).  Enumerating internal consecutive
unions gives exactly (4.4). \(\square\)

The distinct lower-intersection and upper-union q1 palettes are also equal:

\[
 \{X_i\cap X_{i+1}\}=\{Y_i\cap Y_{i+1}\}=\{a,b,c,z\},           \tag{4.5}
\]

\[
 \{X_i\cup X_{i+1}\}=\{Y_i\cup Y_{i+1}\}
                       =\{abz,bcz,acz\}.                         \tag{4.6}
\]

Their multiplicities are not equal.  The lower lists are
\((a,z,b,c,c)\) and \((b,b,c,z,a)\).  At width two the upper lists are
\(abz^2,bcz^2,acz\) and \(abz,bcz^2,acz^2\), respectively.  At
width three, target \(abz\) in \(X\) is exchanged for \(acz\) in \(Y\).
Hence Theorem 4.1 is exactly a support/coverage theorem.

Both phases also contain an internal singleton positive run of coordinate
\(z\).  Every one of the six physical pairs in (5.3) is obtained by active
coordinate relabelling/reversal and has the same obstruction.  Thus
residence depth at least two fails for all six without an
expanded/rethreaded buffer.

## 5. Exact fixed-4 serialization count

Each matching phase has

\[
                              3!\,2^3=48                           \tag{5.1}
\]

serializations obtained by ordering its three edges and orienting each
edge.  Comparing all \(48^2=2304\) pairs by the four deck rows in (1.2)
gives:

\[
\begin{array}{c|c}
(\text{non-Johnson adjacencies among the five old path steps},
 \text{ among the five new path steps})
 &\text{deck-transparent pairs}\\ \hline
(0,0)&6\\
(0,1)&6\\
(1,0)&6\\
(1,1)&6.
\end{array}                                                       \tag{5.2}
\]

Thus exactly \(24\) pairs pass, all with equality in the three decks.  The
six \((0,0)\) pairs are obtained from (0.1) by cyclically relabelling
\(a,b,c\) and by simultaneous reversal.  Written out, they are:

\[
\begin{array}{c|c}
ab,az,bz,bc,cz,ac&ab,bz,bc,cz,az,ac\\
ab,az,ac,cz,bz,bc&ab,bz,az,ac,cz,bc\\
bc,bz,ab,az,cz,ac&bc,cz,bz,ab,az,ac\\
bc,bz,cz,ac,az,ab&bc,cz,ac,az,bz,ab\\
ac,cz,az,ab,bz,bc&ac,az,ab,bz,cz,bc\\
ac,cz,bc,bz,az,ab&ac,az,cz,bc,bz,ab.
\end{array}                                                       \tag{5.3}
\]

The case split is finite and symbolic: every serialization is one of the
\(3!\) edge orders and \(2^3\) orientation rows; comparing its three
distinct-value decks gives (5.2).  Pointwise prefix/suffix equality had only
six passing pairs, all in class \((1,1)\).  Therefore compressed decks are
exactly what creates the six physical \((0,0)\) options.

This is still one fixed active quadruple.  Relabelling \(b,c\) changes the
off-word in (0.1); it does not by itself give \(m^2\) options against one
common incumbent slot.

## 6. Contracted all-six ECO calibration

Use the twelve owners and the two six-edge matchings \(E_0,E_1\) from

\[
\texttt{MATH\_THEOREM\_INDEPENDENT\_ECO\_SIXSEAM\_SIGNATURE\_CONNECTOR\_AND\_FRAGMENT\_LIFT\_20260731.md}.
\]

There are \(25\) common connector perfect matchings which are literal
Johnson matchings and avoid \(E_0\cup E_1\); exactly \(6\) make both phases
Hamilton cycles.  Under the compressed boundary-deck plus internal-OR-deck
criterion:

\[
\begin{array}{c|c}
\text{object}&\text{count}\\ \hline
\text{passing connector matchings}&3\\
\text{passing old/new cut-orientation pairs}&12.
\end{array}                                                       \tag{6.1}
\]

Each passing connector has four linearization pairs.  These are precisely
the three connectors whose internal OR supports were already equal in the
pointwise-signature audit.  The other three exchange one old internal OR
target for one new target, so neither one-way dominance relation holds.

The compressed recensus compares all old/new linearizations of all six
simultaneous literal Hamilton connectors directly; it does not prefilter on
pointwise signature equality.  Its exact rows are frozen in the audit
artifact cited in Section 10.

Thus compressed decks do not increase this particular contracted ECO
connector count; they do provide the smaller six-owner physical
serializations of Section 5.

## 7. Retained-detour calibration

The explicit fourteen-owner retained-detour fixture is obtained by replacing
one common connector edge by a common three-edge Johnson path.  Each phase
has \(28\) linear cut/orientation choices.  The updated exact audit reports,
separately in each direction,

\[
                         0/784                                    \tag{7.1}
\]

pairs satisfying prefix-deck inclusion, suffix-deck inclusion, equal total
union and internal-deck dominance: old-to-new is \(0/784\), and new-to-old
is also \(0/784\).

This is a fixture-scoped no-go.  It proves that a legal retained path can
destroy even coverage-level deck compatibility while leaving endpoint
matching, degree vector and changed-seam count unchanged.  It does not
contradict Theorem 4.1; it shows that expanded ECO path profiles must be
selected structurally.

## 8. Exact remaining construction

The compressed upper gate is now:

1. choose one common incumbent slot and a quadratic \((b,c)\)-menu;
2. make the union of prefix-, suffix-, total-, internal-deck, residence,
   topology, cap and unused-cell failure graphs have vertex-cover number
   \(O(d)\);
3. keep \(O(d)\) physical/local tokens, require every nonprivate exported
   token to have opposite-list/full-atlas exposure \(O(m^3)\) (or the exact
   weighted-anchor bound implying it), and make the unused-cell deletion
   tokens cross-list private.

For pairwise-disjoint immutable slots, these hypotheses give list loss
\(O(md)\); no global upper witness tickets are needed, and the protected row
energy is \(O(dm^3)\).  The \(m^{-2}\) alteration/Haxell extraction then
works for \(d=o(m)\).

The fixed-4 census proves a literal local profile exists.  The retained-
detour \(0/784\) result and the common-incumbent quantifier show why this is
not yet a uniform packet-supply theorem.  Residence and common-cap
compatibility remain independent gates.

## 9. Scope audit

1. Deck inclusion preserves target support, not addresses, multiplicities
   or width grading.
2. Cyclic coverage uses full-cycle intervals in the overlap-or-abut case; otherwise
   add the joint two-ended deck.
3. The fixed-4 six-option count is for serialization/connector choices on
   one labelled C6, not a quadratic \((b,c)\) atlas.
4. The twelve-owner and fourteen-owner counts are finite fixture statements,
   not all-\(m\) supply theorems.
5. Residence is explicitly separate and already fails on the six-owner
   words.
6. No additive-constant or exact-\(B(k)\) theorem is claimed.

## 10. Reproducible audit

Run

```bash
python3 scratch/audit_a_boundary_or_deck_fixed4_connectors_20260731.py
```

It independently checks all \(48^2=2304\) fixed-4 serialization pairs,
recomputes the contracted twelve-owner compressed census, and hash-binds the
fourteen-owner retained-detour replay.  At the time of freezing:

* audit script SHA-256:
  `1b2fb4190010e2f5e94894966d0e625fdcf96d93a305a7c9f94bf1f2dd49e5b1`;
* audit JSON SHA-256:
  `68cb1d72b5845ab6008cd17104e470df6fb386606341266a873b27589a495f20`;
* canonical payload SHA-256:
  `1d622a1911e6ac041e2d39618e3fde7576cdf85dd353d87b42c13b34de9f9ed9`;
* retained-detour source/JSON SHA-256:
  `8d85300da50327a0b99d830b044270287b4d816bc1914a8a9f4e42bbd74b7c17` /
  `3fcd63c04916fe8ed5e3f6b560e778bee9db68723e2d632db25e0504c5912789`.
