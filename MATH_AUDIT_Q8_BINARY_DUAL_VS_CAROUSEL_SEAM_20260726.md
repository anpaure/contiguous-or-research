# Audit: binary-dual compression does not certify Q8 carousel seam coverage

Date: 2026-07-26

Audited sources:

- `MATH_ATTACK_L_Q8_MOVING_ATLAS_BINARY_DUAL_AND_OCCUPANCY_COMPRESSION_20260726.md`;
- `MATH_ATTACK_L_Q8_MOVING_ATLAS_BINARY_DUAL_AUDIT_20260726.md`;
- `MATH_THEOREM_Q8_CAROUSEL_PHASE_SPLICE_SPARSE_SEAM_MACRO_20260726.md`;
- `MATH_AUDIT_Q8_CAROUSEL_AGGREGATE_SEAM_LOSS_20260726.md`.

Method: pure mathematics only.

## 0. Verdict

The two binary-dual reports are correct as written.  They prove an exact
compression theorem for the explicitly restricted pure-shore, one-global-
matching catalogue, and they explicitly decline to extend its fixed-matching
capacity bound to phase-changing or mosaic Q8 columns.

They do **not** prove that a Q8 carousel covers its seam targets.  The binary
one-simplex formula

\[
 \eta^{\rm bin}(R,\Theta)=|R|-\max_{o\in\Theta}|I_o|
 \tag{0.1}
\]

is an exact evaluation of the deficit once the literal support \(I_o\) of
every legal whole option is known.  It does not turn target-by-target
reachability across different options into simultaneous coverage by one
option.

The corrected carousel seam count is quadratic in the protected height:
for carrier owner mass \(G\),

\[
 \sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
 |S_{o,q}^{\epsilon}|
 \le {H(H+1)\over L+1}\,G,
 \tag{0.2}
\]

where \(S_{o,q}^{\epsilon}\) is the distinct literal support contributed by
seam-meeting windows of one carousel option.  Thus discarding every seam
window is justified only when \(L/H^2\to\infty\).  In the intended regime
\(L=O(m)\) and \(H/\sqrt m\to\infty\), this condition is impossible.

Equation (0.2) is an upper bound on uncertified occurrences, not a lower
bound on holes.  It invalidates the sparse-seam quarantine argument but does
not itself refute the carousel.  A positive proof now needs a literal seam
decoder or a simultaneous global packet-cover theorem.  A negative proof
needs a new multiframe capacity invariant; the fixed-one-matching invariant
from the binary-dual report does not apply to a carousel whose payload
segments use several frames.

## 1. Reachability and one-option support differ by an exact synchronization gap

Let \(R\) be any finite tagged target set, let \(\Theta\) be a catalogue of
legal whole options, and let \(I_o\subseteq R\) be the distinct literal
support of option \(o\).  Put

\[
 U:=\bigcup_{o\in\Theta} I_o.
\]

The one-simplex identity gives the exact decomposition

\[
 \boxed{
 \eta^{\rm bin}(R,\Theta)
 =\underbrace{|R|-|U|}_{\text{unreachable targets}}
 +\underbrace{|U|-\max_o|I_o|}_{\text{synchronization gap}}.}
 \tag{1.1}
\]

Consequently, proving that every target is reachable in *some* option kills
only the first term.  It proves simultaneous coverage only if one option
contains all of \(U\), or if a separate integral theorem compiles the
different witnesses into one legal whole option.

This is not a merely formal distinction.  The certified 24-owner,
three-shore Q8 census has a 40-target lower candidate union, while each
shore hits exactly 24 of those targets.  Hence

\[
 |R|-|U|=0,
 \qquad
 |U|-\max_o|I_o|=40-24=16.
 \tag{1.2}
\]

Thus complete potential reachability can coexist with a positive, indeed
linear-at-scale, binary deficit.  The same example occurs explicitly in
both audited binary-dual files and is already a rigorous counterexample to
the inference

\[
 \text{``large moving-atlas candidate union''}
 \Longrightarrow
 \text{``one whole option covers it.''}
 \tag{1.3}
\]

The all-ones dual is therefore a *correct detector* of the synchronization
gap, not a mechanism for removing it.

## 2. Exact carousel seam accounting

One carousel macrocycle has length \(16(L+1)\) and sixteen seam edges.  A
fixed seam edge belongs to exactly \(q\) cyclic windows consisting of \(q\)
transitions.  Hence at signed depth \((q,\epsilon)\), one macrocycle has at
most \(16q\) seam-meeting occurrences.  If the carousel carrier contains
owner mass \(G\), then it contains

\[
 {G\over16(L+1)}
\]

macrocycles.  Therefore, for every whole carousel option \(o\),

\[
 \boxed{
 |S_{o,q}^{\epsilon}|
 \le {q\over L+1}G }
 \qquad(\epsilon\in\{-,+\}),
 \tag{2.1}
\]

because the number of distinct supported targets is at most the number of
literal occurrences.  Summing (2.1) over both signs and all \(q\le H\)
gives (0.2).

Let \(J_{o,q}^{\epsilon}\) denote the support from windows lying wholly
inside payload segments.  The actual support is

\[
 I_{o,q}^{\epsilon}
 =J_{o,q}^{\epsilon}\cup S_{o,q}^{\epsilon}.
 \tag{2.2}
\]

In particular,

\[
 N_q-|I_{o,q}^{\epsilon}|
 \ge
 N_q-|J_{o,q}^{\epsilon}|-{qG\over L+1}.
 \tag{2.3}
\]

Equations (2.1)--(2.3) are the correct interface between the carousel and
the binary support LP.

Three cautions are essential.

1. The \(H/(L+1)\) bound in the carousel theorem concerns starts at one
   maximum depth.  Summing every protected depth costs \(H(H+1)/(L+1)\),
   not \(O(H/L)\).
2. The right side of (0.2) is not known to consist of distinct holes.
   Collisions may reduce distinct seam support, and other packets may cover
   the same targets.  Therefore the \(H^2\) correction is not a no-go
   theorem.
3. At one Gaussian depth \(q=A\sqrt m\), if \(L=\Theta(m)\) and \(G\le W\),
   then the seam support is only \(O(W/\sqrt m)=o(W)\).  Thus a linear
   nonseam deficit at one such depth would survive the seam correction.
   No such multiframe nonseam deficit has yet been proved.

## 3. Why the pure-shore occupancy obstruction cannot simply be imported

The lower bound \(D_{m,q}\) in the binary-dual report classifies every
nonexceptional window relative to one physical perfect matching \(M\).  A
whole pure-shore option is subordinate to that same \(M\) everywhere.

A carousel option instead places different payload segments in different
frames.  Even away from seams, its windows are certified only relative to
the frame of their own segment.  There is no single matching with respect
to which all nonseam targets share the full/empty-pair type used in the
proof of \(D_{m,q}\).  Consequently one cannot set

\[
 L_q^{\epsilon}=|S_{o,q}^{\epsilon}|
\]

in the robust pure-shore inequality and conclude a carousel obstruction.
Doing so would silently apply a fixed-matching capacity theorem outside its
hypotheses.

The source files avoid this error: both binary-dual reports explicitly say
that a phase-changing or mosaic compiler must be audited afresh.

## 4. Exact remaining positive theorem

Let \(\Theta^{\rm car}_{m,L,H}\) be the catalogue of legal whole carousel
options, with one common option used at every signed depth, and put

\[
 R_H=
 \{(q,\epsilon,T):1\le q\le H,\ \epsilon\in\{-,+\},\
 T\text{ is a signed depth-}q\text{ target}\}.
\]

The required theorem is precisely

\[
 \boxed{
 \exists o_m\in\Theta^{\rm car}_{m,L_m,H_m}:
 \sum_{q=1}^{H_m}\sum_{\epsilon\in\{-,+\}}
 \bigl(N_q-|J_{o_m,q}^{\epsilon}
             \cup S_{o_m,q}^{\epsilon}|\bigr)
 =o(W). }
 \tag{4.1}
\]

Equivalently,

\[
 \max_{o\in\Theta^{\rm car}}|I_o|=|R_H|-o(W),
 \tag{4.2}
\]

so the exact binary one-simplex deficit is \(o(W)\).

A seam-decoder theorem would prove (4.1) by showing that the seam supports
fill almost all holes left by the internal payload supports:

\[
 \sum_{q,\epsilon}
 \left|
   \bigl(\mathcal T_q^{\epsilon}\setminus
         J_{o,q}^{\epsilon}\bigr)
   \setminus S_{o,q}^{\epsilon}
 \right|=o(W)
 \tag{4.3}
\]

for one legal common option \(o\).  Targetwise potential reachability,
averaged occurrence load, or a union over different carousel options is
strictly weaker than (4.3).

If carousel pieces overlap in owner supply and are to be selected
independently, the correct alternative is the packet-master LP with its
owner equations and free owner prices.  The one-simplex identity cannot be
used after deleting those constraints.

## 5. Exact remaining negative theorem

A fixed-depth capacity cut would close the carousel lane.  It is enough to
prove that for some fixed \(A,c>0\), with \(q=\lfloor A\sqrt m\rfloor\),
every legal whole carousel option satisfies

\[
 \boxed{
 |J_{o,q}^{-}|+|J_{o,q}^{+}|
 \le 2N_q-cW. }
 \tag{5.1}
\]

When \(L=\Theta(m)\) and \(G\le W\), (2.1) then gives

\[
 |I_{o,q}^{-}|+|I_{o,q}^{+}|
 \le2N_q-cW+o(W),
 \tag{5.2}
\]

and hence a linear binary deficit.  Proving (5.1) requires a joint
four-frame occupancy or projection invariant.  The existing single-frame
quantity \(D_{m,q}\) does not establish it.

An even stronger direct counterexample would prove (5.2) without splitting
seam and nonseam supports.  Conversely, failure to find such a cut is not a
positive proof: (4.1) remains the exact target.

## 6. Source disposition

No correction to either audited binary-dual source is warranted.  Their
scope boundary is accurate, and their 24-owner example already records the
reachability/synchronization distinction.

The carousel macro theorem has already been corrected in its own text and
in the aggregate-seam audit: its \(H/(L+1)\) estimate is a fixed-depth
start fraction, while aggregate quarantine costs \(\Theta(H^2/L)\).  The
remaining issue is not another dual compression.  It is the literal-support
theorem (4.1), or the multiframe capacity counterexample (5.1).
