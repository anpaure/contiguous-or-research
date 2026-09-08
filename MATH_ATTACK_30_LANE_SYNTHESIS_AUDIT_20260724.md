# Adversarial audit of the thirty-lane mathematical synthesis

Source audited: MATH_ATTACK_30_LANE_SYNTHESIS_20260724.md

Date: 2026-07-24

This is a symbolic and provenance audit. I checked the synthesis against the
corrected primary reports, their appended or separate audits, the first-wave
synthesis, the exact-status audit, and items 1370--1397 of
MATHEMATICAL_HANDOFF.md. I did not run a finite search or use a solver.

## 1. Executive verdict

The synthesis has the right high-level mathematical status:

* none of the thirty lanes proves coefficient one;
* none changes a certified interval for \(1\le k<20\);
* DRAY is an unproved sufficient theorem and, if proved, implies coefficient
  one through the audited hook and four-block reductions;
* \(\mathrm{AD}_A\) is an unproved sufficient theorem and, if proved for every
  fixed \(A\), gives a direct literal coefficient-one construction;
* the displayed finite table, DRAY formula, hook identity, cubic-shell
  length, adaptive-MTF length bound, exact-factor overload inequalities, and
  Graver comparison rate are numerically correct in their native
  normalizations.

The note nevertheless needs material correction before it can be treated as
an exact audited synthesis. The principal issues are scope and logical
quantifiers, plus one cross-lane normalization error.

1. **Odd and even normalizations are conflated.** Section 5 fixes
   \(W=\binom{2m+1}{m}\) for odd exact wreath factors. Section 5.3 then uses
   the necklace theorem, whose \(W\) is instead \(\binom{2m}{m}\) and which is
   a direct even-dimensional construction, not an exact-factor endgame.
   Under the section's odd \(W\), the displayed necklace coefficient would
   be \(\sqrt\pi/(2e)\), not \(\sqrt\pi/e\). Section 4 also needs its own even
   normalization stated explicitly.

2. **The two highlighted objects are sufficient routes, not an exhaustive
   characterization.** The assertions that the “surviving obstruction” has
   exactly two forms and that the broad problem “can now be replaced” by two
   objects are not proved. The same note retains distinct sufficient routes
   through LM\(_A\), RFEN, SCOV\(_A\), Packet-Gain, FG\(_A\), and
   RSCD\(_A\). An arbitrary literal word need satisfy neither DRAY nor the
   canonical adaptive-MTF forest condition.

3. **The finite structural sentence conflates two different scopes.**
   Endpoint-fork stability constrains one fixed selection of witnesses, and
   its double-fork conclusion uses the recorded rank cap. Lift-slack
   constrains one-bit lifts with a specified high/low run pattern; it does
   not constrain every equality witness. At \(k=11\), the “hundreds of
   double forks” statement is valid only with the fixed-witness and rank-cap
   hypotheses.

4. **The adaptive-MTF paragraph omits essential data.** Its forest must be
   a spanning Johnson **linear** forest in \(J(2m,m)\). The quantity \(e\)
   must count certified edges whose lower colours are mutually distinct and
   whose upper colours are separately mutually distinct. The short runs
   are internal positive runs and one cuts their entry edges. Finally, the
   improvement from \(O(H^2\rho_H)\) to \((2H+1)\rho_H\) is the explicit
   physical reset charge only; the adaptive support defects can still
   deteriorate on an \(H^2\rho_H\) scale.

5. **The rotor claim in lines 271--274 is not what the rotor theorems prove.**
   Exact orbit scaling settles the divisibility, colour-count, connector,
   and Euler-routing problem. It does not make initialization vanish:
   every physical circuit is initialized and the separate charge is at most
   \(2Q\Phi\). Nor do the cited rotor results say that “lower cores” or
   “coordinate pins” vanish. The remaining theorem is one full SCD with
   integral low ordered-Hall/path-forest toll, with all initialization and
   reset costs charged.

6. **The list of allegedly “solved non-obstructions” needs relaxation
   qualifiers.** Fractional balance is available for the averaged/mobile
   target, but an explicit balanced prescribed quota can lie outside the
   nonnegative fractional exact-factor cone. Quota divisibility and nested
   ownership are solved by an abstract integral flow only before cyclic
   packaging. Coherent harmonic contraction is solved, but the positive
   component/wall noise is not. Reset **accounting** is exact, but obtaining
   sublinear reset/path-forest toll is still an unproved route-specific
   theorem. Thus lines 28--33 are a useful diagnosis, not a theorem that
   these features can be discarded in every formulation.

With these corrections the synthesis is a reliable map of sufficient
routes and architecture-local obstructions. Without them it overstates
necessity and mixes two different meanings of \(W\).

## 2. The required normalization split

Three major parts of the note use two different central layers.

For the odd exact-factor/MWB lanes, use

\[
n_o=2m+1,\qquad
W_o=\binom{2m+1}{m},\qquad
N_{q,o}=\binom{2m+1}{m-q},\qquad
c_{q,o}=\left\lfloor\frac{W_o}{N_{q,o}}\right\rfloor .
\tag{2.1}
\]

For the direct even adaptive-MTF, necklace, and rotor/SCD constructions, use

\[
W_e=\binom{2m}{m},\qquad
N_{q,e}=\binom{2m}{m-q}.
\tag{2.2}
\]

They are related by

\[
W_o=\frac{2m+1}{m+1}W_e,\qquad
W_e=\left(\frac12+O(m^{-1})\right)W_o.
\tag{2.3}
\]

Consequently the audited necklace theorem is

\[
E=\left(\frac{\sqrt\pi}{e}+o_{\Pr}(1)\right)W_e\sqrt m.
\tag{2.4}
\]

If it is deliberately rewritten using \(W_o\), it becomes

\[
E=\left(\frac{\sqrt\pi}{2e}+o_{\Pr}(1)\right)W_o\sqrt m.
\tag{2.5}
\]

Thus line 212 is correct only if Section 5.3 locally redefines \(W=W_e\).
More conceptually, Section 5.3 should be moved out of “Exact-factor
endgames”: Packet-Gain directly constructs an even literal word and bypasses
odd exact-factor MWB/SYNC.

Section 4 likewise needs the declarations

\[
W=W_e=\binom{2m}{m},\qquad
N_1=N_{1,e}=\binom{2m}{m-1},\qquad J=J(2m,m).
\tag{2.6}
\]

## 3. Formula and finite-status ledger

| Synthesis claim | Audit result | Exact qualification |
|---|---|---|
| No coefficient-one proof and no changed \(k<20\) interval (14--20) | **Valid** | No lane closes an unproved positive gate. |
| \(\nu(1),\ldots,\nu(10)\) and \(\nu(12)\) (37--42) | **Valid** | Nonzero-mask convention. |
| Eight open intervals (44--57) | **Valid** | Exactly the intervals in handoff item 1375 and the exact-status audit. |
| Add one for the all-mask convention (60) | **Valid** | For the stated positive dimensions; \(\nu(0)=0\) may be added if “every \(k<20\)” is meant to include \(k=0\). |
| DRAY formula (75--79) | **Valid as an unproved hypothesis** | Fixed primitive \(0<a<b\), \(c>2b\). |
| DRAY width \((at+1)(bt+1)\) (81--82) | **Valid** | Since \(c>2b>a+b\), hence \(ct\ge at+bt\). |
| Hook identity \(P_rP_s=P_{r+s}+uP_{r-1}P_{s-1}\) (89--93) | **Valid** | The recursive shifted-child identity and exact width telescope are audited. |
| DRAY \(\Rightarrow g_4-w_4=o(R^3)\Rightarrow \nu(k)=W(k)+o(W(k))\) (84--98) | **Valid** | Zero-side children use the slice word; long-chain tails require truncated zeroth and third moments. |
| Cubic shell length (104--109) | **Valid** | For the repaired \(t=1\) boundary word. It has leading factor two. |
| Ring/raster/shell no-go claims (111--113) | **Valid only as architecture-local claims** | The ordered-factor case means the occurrence-by-occurrence noncrossing endpoint model, not every factorization of the shell word. |
| Adaptive-MTF no-short-positive-run iff (117--121) | **Valid** | A local theorem for a finite Johnson walk, with \(H\le m/2\); fixed \(A\) satisfies this for large \(m\). It gives no global support distinctness or cyclic closure. |
| \(\mathrm{AD}_A\) conditions (125--138) | **Valid as an unproved sufficient statement after definitions are repaired** | Use one oriented spanning Johnson linear forest and certified \(e\) as in Section 6 below. |
| Adaptive-MTF length bound (140--146) | **Valid** | It is the canonical-support upper bound; incidental and cross-component intervals may improve it. |
| Unconstrained splicing gives \(Hc=o(W)\) (148--151) | **Valid** | A maximal endpoint splice forest has \(c\le W_e/m\), but splicing may create short runs and deep-support collisions. |
| Linear short-run toll (153--154) | **Needs scope correction** | Linear only for the explicit physical reset term, not necessarily for the total support loss caused by cutting. |
| Fixed-window \(c_q\) are bounded (158--162) | **Valid** | In the odd exact-factor normalization and for fixed \(A\). |
| \(M_q(F)\le O_q(F)/c_q\) (166--168) | **Valid** | Here \(M_q\) is the missing-target count; it should be defined. |
| Floor energy dominates overload (169--170) | **Valid** | In the report notation \(O_q\le\Phi_q\), equivalently \(Q_q\ge2O_q\) when \(Q_q=2\Phi_q\). |
| Fixed-window overload diagonalizes to MWB (171--172) | **Valid after definition** | It must mean \(\sum_{q\le H_A}O_q/c_q=o(W_o)\) for every fixed \(A\), not merely \(O_q=o(W_o)\) separately for each fixed \(q\). |
| Coherent contraction \(1-2/n\) per greedy transposition (179--183) | **Valid** | A word of \(O(n)\) frozen transpositions gives constant squared-norm contraction; component/wall noise remains. |
| RFEN implication (185--190) | **Valid conditionally** | Correct annealed RFEN selects integral leaves and gives \(O_A(H_A\operatorname{Cat}_m)=o(W_o)\); it is not necessary for MWB. |
| Nested lower-bounded flow (194--197) | **Valid in the stated noncyclic model** | It removes abstract integrality/divisibility/nesting/common-root obstructions, not cyclic packetization or exact-factor positivity. |
| Adaptive-Hall abstract recourse claims (199--205) | **Valid with the stated disclaimer** | The cube and sibling-rewire examples are not packetized exact factors. |
| Necklace collision constant (209--213) | **Misnormalized in context** | Correct as (2.4), with probabilistic \(o_{\Pr}(1)\), not deterministic \(o(1)\). |
| Two-necklace switch (215--218) | **Valid after scope correction** | Requires \(\ell\ge3\), common type/core/exterior/outside trace/phase, and gives rectangles at every **certified** deeper rank. |
| Packet-Gain implication (220--224) | **Valid conditionally** | Direct even-word route; sufficient, not equivalent to MWB. |
| Graver \(1/\operatorname{Cat}_m\) gap improvement (228--232) | **Valid** | Comparison with an existing better positive endpoint; no bound on the optimum. |
| Bad prescribed quota and negative mass (234--238) | **Valid** | A prescribed-quota obstruction, not a mobile-MWB lower bound. |
| Signed-face entropy dual (266--269) | **Valid in that repair architecture** | In its odd exact-factor normalization, the hereditary peeling equivalence assumes \(|\mathcal H|=O(W_o)\) and concerns every linear-sized residual. |

No displayed arithmetic identity other than the contextual interpretation of
the necklace constant fails. The errors are principally omitted hypotheses,
undefined symbols, and invalid necessity rhetoric.

## 4. Correct implication structure

The following arrows are audited.

\[
\mathrm{DRAY}
\Longrightarrow
\text{uniform dominant four-box excess }o(R^3)
\Longrightarrow
\nu(k)=W(k)+o(W(k)).
\tag{4.1}
\]

\[
\mathrm{AD}_A\text{ for every fixed }A
\Longrightarrow
\text{direct even literal central-band word}
\Longrightarrow
\nu(k)=W(k)+o(W(k)).
\tag{4.2}
\]

For odd exact factors,

\[
\begin{array}{c}
\mathrm{LM}_A\quad\text{or corrected RFEN}\quad
\text{or }\mathrm{SCOV}_A\quad
\text{or a joint same-transposition SDP/coherence lemma}
\\[1mm]
\Downarrow\\[-1mm]
\displaystyle
\sum_{q\le H_A}\frac{O_q(F)}{c_q}=o(W_o)
\\[2mm]
\Downarrow\\[-1mm]
\mathrm{MWB}
\Downarrow
\nu(k)=W(k)+o(W(k)).
\end{array}
\tag{4.3}
\]

Other direct sufficient routes include Packet-Gain, FG\(_A\), and
RSCD\(_A\). Their antecedents remain unproved.

None of the following converse or necessity claims is established:

* coefficient one \(\Rightarrow\) DRAY;
* coefficient one \(\Rightarrow\) \(\mathrm{AD}_A\);
* MWB \(\Rightarrow\) LM\(_A\), RFEN, SCOV\(_A\), Packet-Gain, or labelled
  synchronization;
* failure of one route-specific lemma \(\Rightarrow\) failure of coefficient
  one;
* every successful proof must select an exact factor;
* every successful direct word must use the canonical adaptive-MTF core.

Accordingly, the Section 5 heading “one positive gate,” lane X's phrase
“DRAY strictly implies,” and the two-object bottom line should not be read
as logical equivalences. “DRAY implies” is proved; strict nonimplication in
the reverse direction is not.

## 5. Finite-status and finite-structure correction

The numerical table in Section 2 is exact. Its structural follow-up should
be split into two statements.

First, if a word in odd dimension \(k=2m+1\) has length \(M+d\), fixed
witnesses for the two middle ranks have at least \(M-3d\) common two-sided
endpoint positions. **Under the recorded rank cap**, all but at most
\(4d-h\) low positions are double-fork junctions in the selected directed
linear forest. At \(k=11\), this gives at least \(319+h\) double forks,
including the audited low-entry-rank and coordinate-omission subcounts.
These facts concern one fixed witness selection and are not yet
inconsistent.

Second, the lift-slack theorems concern a word obtained by tagging a lifted
base word. For old target rank \(r\), \(M=\binom{k}{r}\), and \(q\) high
runs, they give

\[
|W_{\rm lift}|\ge
2M-r\left(\binom q2+3q\right),
\tag{5.1}
\]

with the one-transition strengthening \(2M-r\). The coefficient is old
rank \(r\), not ambient dimension \(k\). At the current even-to-odd finite
steps the minimum certified run counts are \(5,9,17,31\). This is a
run-count/high-mass tradeoff, not a theorem that every equality witness has
simultaneously many long runs.

Therefore lines 63--67 should not say that endpoint-fork **and** lift-slack
constrain “any equality witness.” Only the first theorem applies directly
to a general near-equality word, and even there the fixed-witness/rank-cap
qualifiers are essential for the fork conclusion.

## 6. Adaptive-MTF correction

The corrected standalone statement is as follows. Let

\[
W=W_e=\binom{2m}{m},\qquad
N_1=\binom{2m}{m-1},\qquad
H=\lceil A\sqrt m\rceil,
\]

and work in \(J(2m,m)\). Choose an oriented spanning Johnson **linear**
forest. Let \(e\) be the number of certified forest edges such that their
lower colours are pairwise distinct and their upper colours are separately
pairwise distinct. Distinct ordered lower-upper pairs alone are
insufficient for the term \(2(N_1-e)\).

Let \(\rho_H\) be the number of **internal** positive coordinate runs of
length at most \(H\), and cut the entry edge of each such run. With compatible
cut-boundary dummies and residual orders, the canonical-support construction
satisfies

\[
L_{\rm band}\le
W+(2H+1)(c+\rho_H)+2(N_1-e)
+\sum_{q=2}^{H}
(\widetilde M_q^-+\widetilde M_q^+).
\tag{6.1}
\]

The displayed \(\mathrm{AD}_A\) conditions then imply (6.1) is \(W+o(W)\).
This implication is valid. The tilded quantities are the missing supports
of the chosen canonical adaptive flags; they depend jointly on orientation,
cuts, dummies, and residual orders. They are not functions of the
unoriented forest alone, and are not necessary defects for an arbitrary
optimal literal completion.

The accurate short-run conclusion is

\[
\text{explicit reset charge per cut}=2H+1
\quad\text{rather than}\quad H^2+2H.
\tag{6.2}
\]

It is not an unconditional \(O(H\rho_H)\) bound on all loss caused by
cutting. The support-defect sum in (6.1) is precisely where an
\(H^2\rho_H\)-scale deterioration can remain.

The compact prompt in lines 325--332 needs the same repairs: “spanning
Johnson linear forest,” certified separate lower/upper colour distinctness,
and “cut the entry edge of every internal short positive run.”

## 7. Scope audit of the no-go and repair sections

The bullets in Section 6 are safe only with the following scopes.

* The isolated-reset ABKV ceiling is an older audited result (handoff item
  1353), not a new conclusion of items 1370--1397. It applies only to the
  scoped one-reset-per-atom ABKV certificate.
* A profile-3 \(C_8\) switch changes a fixed-\(A\) objective by \(O_A(m)\), so
  \(o(\operatorname{Cat}_m)\) such bounded local switches cannot repair a
  linear defect. A positive-density rebundling **or another coarse/nonlocal
  construction** is needed before this particular cleanup can finish. No
  theorem says every proof must rebundle first.
* The independent-occupancy failure is for the audited canonical independent
  typed Bernoulli model, with its fixed-tuple factorization and small maximum
  inclusion probability. It is not a theorem about every randomized
  middle-matching algorithm.
* The \(o(W)\)-appendage obstruction is also an older endpoint-throughput
  theorem (handoff item 1358). It applies when one rank has more holes than
  the appendage length; an \(o(W)\) appendage may repair \(o(W)\) vertically
  aligned holes per rank.
* Point margins, Johnson support, Hall feasibility, and signed saturation
  are individually insufficient in the particular abstract selector,
  Boolean-owner, or signed-lattice relaxations where the counterexamples are
  built. Those examples are not positive packetized exact factors.
* The triangular-shell “globally ordered factor” is specifically the model
  in which every virtual occurrence is assigned an interval and both
  endpoint orders follow shell-word order. Crossing endpoints, a new middle
  order, and occurrence rebundling remain open.

The final sentence of Section 6 correctly says these are not general lower
bounds. The preceding bullets should carry their scopes locally rather
than rely on that final disclaimer to repair overbroad wording.

For signed-face repair, the entropy dual and same-rank obstruction are exact
inside that repair architecture. The “exact dense-face peeling target” is
the asymptotic equivalence, under \(|\mathcal H|=O(W_o)\), between sublinear
repair cost and unbounded economical-face density in every linear-sized
residual. It is not a necessary condition for MWB or an arbitrary literal
word.

For rotor/SCD, replace lines 271--274 by the following:

> Exact integer orbit scaling settles the divisibility, colour-count,
> connector-pairing, and Euler-routing part of the rotor construction. Every
> physical circuit is nevertheless initialized separately, with the audited
> charge \(Q\sum_d(2d+2)p_d\le2Q\Phi\). The remaining rotor/SCD problem is
> one full integral SCD with optimized fixed-window ordered-Hall/path-forest
> toll \(o(W_e)\); it is not a fractional routing obstruction.

This is what handoff items 1373 and 1386 prove. “Lower cores” and
“coordinate pins vanish” should be deleted unless a separate theorem and
definition are supplied.

## 8. Lane-by-lane ledger audit

| Lane | Result | Required reading of the synthesis row |
|---|---|---|
| A | **Pass with scope** | Exact profile-3 partner/mass counts; only \(o(\operatorname{Cat}_m)\) bounded fixed-\(A\) cleanup is ruled out. |
| B | **Pass** | Signed trade/lattice connectivity supplies no positive factor or common owner flow. |
| C | **Pass** | Exact component Max-Cut identity; positive cut remains open. |
| D | **Pass** | Aggregate/orbit averages do not select a single positive exact factor. |
| E | **Pass with scope** | Rank-isolated adjacent swaps are exact, but the Hall graphs are endogenous and evolve with earlier choices. |
| F | **Qualify** | Primitive-ray reduction is valid; only the audited random/intact-side/short-run/additive-slab braid architectures pay quadratic loss. |
| G | **Pass after Section 7 repair** | Exact optimized path-forest toll and canonical-SCD failure; initialization does not vanish. |
| H | **Pass with scope** | Compact four-box gate and surface/portal barriers are architecture-local. |
| I | **Pass with scope** | Exact signed-face entropy dual; same-rank defect obstruction is for that repair architecture. |
| J | **Pass** | Integral signed selector surjectivity removes lattice index only, not positivity/support/quota. |
| K | **Pass** | The exhibited deep-suffix tail subcube is shallow-inert; no theorem covers the whole Catalan cube or exceptional shallow choices. |
| L | **Pass** | Exact parity restitution; LM\(_A\) remains a sufficient route-specific gate. |
| M | **Pass** | Frozen-word harmonic and wall calculus exact; RFEN remains unproved and is not necessary for MWB. |
| N | **Pass with scope** | Carry/rewire calculus exact; exponential recourse examples are abstract and not exact-wreath packetizations. |
| O | **Pass with scope** | Split flow exact; the irreversible-prefix obstruction is for arbitrary integral Boolean owner systems, not proved for exact factors. |
| P | **Pass** | The \(2q\) capacity envelope is an upper envelope, with no attainment, productive sign, or cancellation theorem. |
| Q | **Pass** | Coupled lower/upper colour tower exact; no depth-one-to-Gaussian bootstrap follows. |
| R | **Pass with scope** | Local alternating-\(C_8\) balance exact; initial PBBS density, compatible cancellation, and cleanup remain unproved. |
| S | **Pass with scope** | SCD extension and ordered-Hall formula exact; the Gaussian obstruction is only for one fixed global coordinate frame. |
| T | **Qualify wording** | Factor-two shell word exact; ring/raster/occurrence-ordered-factor obstructions are local to those models. |
| U | **Pass with scope** | The larger spill family is literal; the cubic portal toll is local to the all-literal-balanced portal architecture. |
| V | **Pass with scope** | Exact face-cover dual; dense-face criterion uses \(|\mathcal H|=O(W_o)\) in the odd exact-factor lane and is route-specific. |
| W | **Correct normalization and scope** | Direct even-dimensional Packet-Gain route; use \(W_e\), \(o_{\Pr}(1)\), and “every certified deeper rank.” |
| X | **Replace “strictly implies”** | DRAY implies coefficient one. No reverse nonimplication theorem has been proved. |
| Y | **Pass** | Exact projection/stationary dual; a low stationary class is a sufficient, not necessary, route. |
| Z | **Pass with wording** | Standard M/M-natural/L-natural convexity fails in the audited domains; augmented-Graver local/global comparison is exact. |
| AA | **Pass with scope** | Exact floor hierarchy/SDP bounds; any sufficient coherence lemma must use the same transposition for gain and loss. |
| AB | **Pass** | Leakage/fragmentation identities are exact and orientation-blind statistics alone give no favorable sign. |
| AC | **Pass** | Graver descent reaches the positive optimum relative to a comparator; it gives no \(o(W_o)\) bound on that optimum. |
| AD | **Qualify** | No-short-positive-run iff and canonical word bound are exact; only the explicit reset toll is proved linear, and \(\mathrm{AD}_A\) remains open. |

Thus every row has genuine audited content. The rows needing actual wording
changes are F, G, T, V, W, X, and AD; several others need their model scope
kept visible.

## 9. Corrected bottom line

The first boxed object should say

\[
\boxed{\text{an asymptotically width-optimal dominant three-box braid}}
\]

rather than “width-optimal,” because DRAY allows an \(o(t^2)\) excess.

The second should say

\[
\boxed{\text{an oriented Johnson linear forest with low reset and
canonical-support toll}}
\]

and be read as the canonical adaptive-MTF sufficient route. It encodes the
MTF legality, certified first-band colours, boundary dummies, and selected
deep supports exactly within that architecture. It does not characterize
all factorability or pin survival for arbitrary literal words.

A safe replacement for lines 339--355 is:

> The attack did not close the conjecture, but it produced two especially
> compact new sufficient endgames: DRAY and the adaptive-MTF forest lemma
> \(\mathrm{AD}_A\). DRAY is the cleanest local box theorem; \(\mathrm{AD}_A\)
> is the closest of the two to a direct literal global construction. They
> are not known necessary, and the factor-heat, Packet-Gain, signed-face, and
> rotor/SCD routes remain distinct sufficient alternatives.

That formulation preserves the genuine shortening achieved by the thirty
lanes without promoting two proposed routes to an exhaustive theorem.

## 10. Final classification

* **Finite numerical status:** accepted without endpoint changes.
* **DRAY formula and implication:** accepted as an unproved sufficient gate.
* **Adaptive-MTF theorem and implication:** accepted after the linear-forest,
  certified-colour, internal-run, even-\(W\), and reset-charge qualifiers.
* **Odd exact-factor formulas:** accepted after defining weighted
  fixed-window overload.
* **Packet-Gain section:** accepted only after separating the direct even
  normalization and restoring probabilistic/certified-rank scope.
* **No-go inventory:** accepted as a collection of method- or
  architecture-local statements, not a universal obstruction theorem.
* **Rotor summary:** requires substantive replacement.
* **“Only two objects” rhetoric:** unsupported as necessity; replace by “two
  especially compact sufficient endgames.”

The synthesis therefore passes as a conditional research map after the
listed repairs, but not verbatim as an exact implication ledger.
