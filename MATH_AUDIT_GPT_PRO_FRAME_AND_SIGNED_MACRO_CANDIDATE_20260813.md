# Audit of the GPT-Pro frame and signed-macro candidate

**Date:** 2026-08-13  
**Source attachment:**
`/Users/amir.nuriyev/.codex/attachments/4db2edd8-d89f-48d3-9505-72e9701eee08/pasted-text.txt`  
**Source SHA-256:**
`b4ebfb1afcb3b6dbe65714ff8c7db94c3867d6d70bcbe97717b51503ca214fd2`  
**Verdict:** **FAIL** as a proof or one-conditional reduction of
\(\nu(k)\le B(k)+O(1)\).

The earliest decisive failure is Theorem A's use of Q4: the cited host
theorem does not imply BH1--BH4.  Independently, Theorem D's pointed identity
is algebraically correct but is only the original \(Y_H\)-shore exchange,
not a one-owner absorber.  Several other quoted inputs are strengthened
beyond their proved quantifiers.

## 1. Theorem D

Write the defining signed macro canonically as

\[
 D^+-D^-=Y_H=Y_H^+-Y_H^-,
 \qquad \min(Y_H^+,Y_H^-)=0.
\]

If

\[
 R_0=\min(D^+,D^-),
\]

then coefficientwise uniqueness indeed gives

\[
 D^+=Y_H^++R_0,\qquad D^-=Y_H^-+R_0.
\]

With the repository definitions

\[
 B^+=Y_H^-,\qquad B^-=Y_H^+-e_H,
\]

the displayed identities

\[
 R_0\sqcup B^+=D^-,
 \qquad
 R_0\sqcup B^-\sqcup\{H\}=D^+
\]

are correct when the two defining shores are simple.  The point projections
of \(\Phi_u, K,\Delta_x\), and \(Y_H\) are also computed with the correct
signs.

However, the current between these two states is

\[
 D^+-D^-=Y_H,
\]

not \(e_H\).  The residual needed to turn the signed macro into a one-owner
positive absorber is exactly

\[
 Z_H=e_H-Y_H=B^+-B^-.
\]

Thus the pointed identity does not close the residual; it merely rewrites
the two shores of the original signed \(Y_H\)-current after extracting their
common part.  Calling it “precisely the absorber functionality” reverses the
logical role of \(B^+-B^-\).

The attachment itself derives the obstruction correctly: an unpointed
defining-deck identity in the requested orientation would force
\(Z_H=\pm Y_H\), hence \(2Y_H=e_H\) or \(e_H=0\).  That observation confirms,
rather than removes, the missing conformal lift of \(Z_H\).

There is also a proof-strength issue in the Avoidance Lemma's use.  A first
moment argument avoids any already fixed polynomial forbidden owner bank,
but does not by itself prove simultaneous simplicity of every defining deck
unless the previously chosen complete decks and both signs are included in
the forbidden list at every greedy step.  This repair is available for the
bounded star and was already carried out more carefully in the repository;
it does not change the decisive sign issue.

## 2. Proposition 1 and the frame

The union identity

\[
 H_s\cup\cdots\cup H_t
 =A_s\cup\cdots\cup A_{t+q-1}
\]

is correct.  The number of intervals of length at most \(d\) in a word of
length \(W+d\) is also exactly

\[
 \sum_{w=1}^d(W+d-w+1)
 =dW+\binom{d+1}{2}.
\]

But the definition's claimed equivalence is false without an additional
structural hypothesis.  Merely requiring

\[
 |A_t\cup\cdots\cup A_{t+q-1}|=r
\]

does not imply that the \(q\) distinguished toggles are distinct, disjoint
from one local core, or that the sprays union to exactly that core.  Nor does
it imply that every shorter interval has rank at most \(r-1\).  Proposition
1 is valid only after placing the stronger literal aperture decomposition in
the hypotheses.

Lemma 3's \(d=\Theta(\sqrt k)\) conclusion is standard and compatible with
the repository, but the displayed constants are supported only by a sketch;
the attachment does not supply the explicit inequalities it claims to prove.

Proposition 4 also needs a stronger defect hypothesis.  Deleting one
leftover component containing \(s\) owners may destroy many already selected
lower and upper witnesses.  Charging only its \(s\) owners is valid only if
the stated \(C_2\) target-defect bound is recomputed after deleting every
leftover component, or if the components have certified private witnesses
elsewhere.  That quantifier is absent.

## 3. Theorem A and the quoted inputs

### 3.1 Q4 does not imply BH1--BH4

The actual subexponential low-exposure host theorem says that an already
constructed union of properly phased incidence cycles satisfying

\[
 e_m=2^{o(m)},\qquad\alpha_m=o(m),\qquad\beta_m=o(m)
\]

extends to a spanning two-factor.  It does not produce:

* four visits with one common predecessor toggle tuple \(U\);
* one global source-word phase modulo \(q\);
* fresh pairwise-distinct continuation-prefix sets;
* a shared spray core \(C^*\);
* prescribed placement of visits on ambient Euler components; or
* a literal source-word chronology at all.

Those are BH1--BH4, not conclusions of Q4.  IA-2 is therefore false, and
Theorem A cannot invoke Theorem B from Q4.

### 3.2 Lower flags

The arbitrary-Ferrers theorem proves only capacity-safe containment
matching.  It explicitly states that it does not chainize the matched targets
inside owners and does not construct a literal antecedent.

Moreover, Theorem B fixes one partition

\[
 C^*=\Gamma_0\dot\cup\cdots\dot\cup\Gamma_{q-1}
\]

on a cyclic schedule.  A width-\(w\) lower slot sees one forced union of
\(w\) consecutive \(\Gamma\)-classes.  These core parts are not freely and
independently steerable after the bank is built while retaining every
\(q\)-window core, seam alignment, and switch invariance.  Consequently the
claim “lower-flag demand 0” is unproved.

### 3.3 Upper steering and common cap

The Aug. 7 unified rail-queue theorem proves a symmetric fractional mixture
with all upper ranks covered.  It does not give a terminal integral steering
theorem which avoids an arbitrary \(O(\sqrt k)\) endpoint bank with only
\(O(1)\) named misses.  Q5 is therefore not a proved black box in the form
used by Theorem A.

Likewise Q6 is an equivalence: the typed suffix linkage exists if and only
if the full-port gammoid rank/all-cut condition holds in one fixed occurrence
state.  It does not prove that the cut condition holds after the proposed
bank, prefixes, compensation paths, factor resources, and witnesses are
deleted.

## 4. Further internal issues in Theorem B

Conditional on BH1--BH4, the AP gap calculation and the local inventory of
entry, interior, and exit owners are largely sound.  They do not establish
the full stated interface:

1. Residence is checked for \(Y,U,C^*\), but not for continuation-prefix
   labels \(V\).  BH3 constrains only the first \(q-1\) prefix sets; it does
   not forbid later recurrence which creates a short run or zero gap.
2. A witness which contains a full visit is switch-invariant, but merely
   avoiding an endpoint strictly inside a visit does not guarantee this.  A
   witness can start inside a visit and end in its re-paired continuation.
   Both cuts, or an actual full-union shield before either cut, must be
   controlled.
3. Q4 preserves the protected cycles as saturated factor components.  It
   does not put four visits on chosen ambient components, so local \(S_4\)
   re-pairing does not by itself yield iterative global fusion to one
   component with only \(O(1)\) owner mass discarded.
4. The bank counts \(4(L+q-1)\) associated owner windows for \(4L\) new
   visit letters.  The extra entry windows live in the unproved predecessor
   collars.  The claimed zero-overhead accounting is therefore conditional
   on a global co-counted host, not a consequence of the local AP blocks.

## 5. Theorem C

The fixed-core character and the consistency identity

\[
 M\binom{M-1}{q-1}=q\binom Mq
\]

are correct.  The staircase differences generate the zero-sum subgroup
modulo \(q\) provided the positions can be chosen freely.  This is a group
or character-elimination statement.  It does not prove the stated
“finitely many” positive, owner-disjoint stealing construction in one fixed
fibre, nor compatibility with named compulsory rows.  The attachment's own
table ultimately acknowledges that positive selection remains open.

## 6. Proof-safe verdict

The candidate contains useful local algebra, but it does not reduce the
whole theorem to PS\((k)\).  In addition to PS\((k)\), it still assumes or
leaves open:

\[
 \boxed{
 \text{literal lower chainization}+
 \text{resident word-level host interface}+
 \text{protected global fusion}+
 \text{integral upper steering}+
 \text{typed cap cut}.}
\]

Theorem D does not remove the special \(B^+/B^-\) residual: it identifies
the original signed shore exchange and then mistakes it for the missing
one-owner current.
