# Independent audit of the folded-C8 endpoint one-ray actuator

Date: 2026-08-01  
Lane: K, physical host embedding / compiler transport  
Status: exact scope correction, unconditional nested-prefix transport lemma,
and exact flat/common-cap/charge obstruction.  The one-ray actuator passes;
the combined cross bank and zero-charge regeneration do not follow.

## 0. Verdict

The corrected endpoint construction has two genuine positive pieces.

1. For every `d>=2`, an active endpoint rethread carries one complete nested
   **suffix** ray.  Its new ray occurrences are literally addressed.  Once
   the rethreaded typed source is the actual old source, binary full-block
   refinement transports every admissible old matching cell injectively and
   makes the new side cells disjoint from that image.
2. The separate three-cut/one-seam owner surgery has, on the authenticated
   folded family, two resident path components on all `8d+24` owners and all
   sixteen upper support values.  In the frozen census `2<=d<=12`, their
   sizes are `d+2` and `7d+22`, and their `8d+22` retained lower edge colours
   are distinct.

The stronger combined-cross-bank interpretation is false.  The frozen
common-endpoint census has

\[
 \texttt{exact\_one\_ray\_comparators}=0,
 \qquad
 \texttt{one\_ray\_universal\_support\_actuators}=0
                                                               \tag{0.1}
\]

for every `2<=d<=12`; its common opening has only fifteen upper support
values.  The upper-safe seam is a different owner-factor operation and may
put the transported prefix coordinate on the other component.  Therefore
the endpoint module supplies the old/new opposite suffix shores separately,
not both perfect cross matchings in one cap/guard state.

There are three further load-bearing qualifications.

* Planting the rethreaded prefix is a same-length **thinning**, not a
  full-block refinement.  Full-block transport starts only after the typed
  host has been planted.
* Splitting the endpoint host has raw source charge one.  Its natural
  depth-`d` erosion is not the audited flat owner path.
* Forming coordinatewise unions of the two phase source letters is not a
  common-`Q` proof.  The common source cap must also lie in every incident
  owner envelope and reconstruct every protected row.

Thus the corrected live gate is

\[
 \boxed{\text{typed-host embedding with guarded address transport}}
 \; + \;
 \boxed{\text{complementary prefix shore in the same cap state}}
 \; + \;
 \boxed{\text{one bounded reset/contraction}}.          \tag{0.2}
\]

No separate background Hall problem remains after a genuine admissible
full-block refinement.  The unresolved background issue is exactly whether
the *preceding host-planting step* preserves the cells and guards used by the
old matching.

## 1. The exact nested-prefix transport

The abstract algebra behind the positive one-ray statement is the following.
Let the old endpoint prefix be

\[
 E_0,E_1,\ldots,E_d,
 \qquad E_0\supseteq E_1\supseteq\cdots\supseteq E_d,
                                                               \tag{1.1}
\]

and let the rethreaded letters `Q_0,...,Q_d` satisfy

\[
                         E_i=\bigcup_{t=i}^{d}Q_t
                         \qquad(0\le i\le d).           \tag{1.2}
\]

Outside this prefix the two source words agree.  In the folded endpoint,
the `Q_t` are the decreasing filler rail, clipped by the chosen active
half.  Equation (1.2) is the exact source identity; a target-set identity
without these occurrence positions would not suffice.

For an old interval `[i,j]`, define

\[
 \phi([i,j])=
 \begin{cases}
 [i,d],&j\le d,\\
 [i,j],&j>d.
 \end{cases}                                             \tag{1.3}
\]

Then

\[
                     \operatorname{OR}_E([i,j])
              =      \operatorname{OR}_Q(\phi([i,j])).  \tag{1.4}
\]

Indeed, for `j<=d`, the nested old interval has value `E_i`, while
(1.2) gives the same value on `[i,d]`; for `j>d`, the complete ladder
`[i,d]` is already present and the common suffix contributes identically.

The map `phi` need not be injective on all interval occurrences.  Its only
collisions have a common start `i` and old endpoints at most `d`, and hence
all colliding old cells have the same literal OR value `E_i`.  Consequently:

### Theorem 1.1 (exact-target matching transport)

If an old target-to-cell matching assigns each target to a cell whose
literal OR is exactly that target, then `phi` is injective on the selected
cells and preserves every target.

#### Proof

If two selected cells collide under `phi`, the preceding observation gives
them the same old OR value.  A matching has only one vertex for that target
value, so the two selected cells were the same matching edge.  Equation
(1.4) preserves the target.  \(\square\)

This theorem is enough for an already materialized unguarded OR matching.
It is **not** enough for the matching-first common-cap graph, where two
different prospective targets can use two duplicate cells with the same
minimal core.  It also forgets width, absolute address, occurrence
multiplicity, deadline class and protected pins.

## 2. What full-block transport does and does not prove

After the typed endpoint letter `X` is actually present, write

\[
                         X=F\cup N                       \tag{2.1}
\]

for the far/near oriented split and replace `X` by the consecutive block
`F,N`.  This second map really is a binary full-block refinement.  Its
canonical lift is

\[
 \psi([i,j])=
 \begin{cases}
 [0,j+1],&i=0,\\
 [i+1,j+1],&i>0.
 \end{cases}                                             \tag{2.2}
\]

It is injective and preserves literal OR.  Hence, if every lifted old
matching cell remains admissible, the simultaneous full-block theorem
transports the whole old matching and the new ray side cells are disjoint
from its image.  This is precisely the repository theorem invoked in the
latest rebase.

The antecedent “remains admissible” is not automatic.  In the canonical
nested model, let `A` be the old maximal source, `B` the same-length
rethread, and `C` the split source.  Under the natural index lift from `A`
to `C`, literal OR fails exactly on

\[
             \mathcal T_d={[i,j]:0\le i\le j<d\},
             \qquad |\mathcal T_d|=\frac{d(d+1)}2.      \tag{2.3}
\]

All other

\[
                         \frac{3(d+1)(d+2)}2             \tag{2.4}
\]

old interval cells retain their OR under that natural lift.  Every old
interval starting at the split position also gains one unit of width.
The alternative map `psi o phi` repairs the target values in (2.3), but it
moves them to the long ladder cells.  Therefore it does not preserve a
width deadline or an address guard without a separate check.

More generally, if two same-length words have the same depth-`d` dilation,
then every interval of length at least `d+1` has the same OR in both words:
such an interval is the union of its consecutive `(d+1)`-windows.  If the
words differ only at the first `d` positions, only the `d^2` short cells

\[
       0\le i\le d-1,qquad 1\le |I|\le d              \tag{2.5}
\]

can possibly differ.  Formula (2.3) is the sharper exact triangle for the
folded nested prefix and the natural split lift.

Thus there is no new residual Hall row once `B` is an actual old typed
source with an admissible matching.  Planting `B` from the canonical `A`
is nevertheless not covered by full-block transport; it must use Theorem
1.1 on the exact-value face or a guarded address isomorphism on the compiler
face.

## 3. The split is nonflat and has raw charge one

Let the first old owner be

\[
                         T_0=X\cup B_1\cup\cdots\cup B_d,
                         \qquad |T_0|=r.                \tag{3.1}
\]

After `B_0=X` is replaced by `F,N`, the first two depth-`d` windows are

\[
 \begin{aligned}
 R_0&=F\cup N\cup B_1\cup\cdots\cup B_{d-1},\\
 R_1&=N\cup B_1\cup\cdots\cup B_d .
 \end{aligned}                                         \tag{3.2}
\]

Every later old owner reappears shifted one position.  In the full nested
rail, `R_0` omits the terminal filler and `R_1` omits the far active label,
so both have rank `r-1`.  In any variant one always has

\[
                         R_0,R_1\subseteq T_0.          \tag{3.3}
\]

Therefore if both new rows were required to have rank `r`, (3.3) would
force `R_0=R_1=T_0`, a stutter.  The split cannot itself be a strict flat
rank-`r` realization of the audited owner path.  It can only be used as a
nonflat actuator with its new rows explicitly accepted and compiled, or be
followed by a certified contraction/rethread.

Moreover

\[
                         |C|=|B|+1.                    \tag{3.4}
\]

Deleting and reconnecting owner-factor edges does not delete a source
letter.  Hence the displayed local actuator has raw `chi=1`.  A zero-charge
use requires an independently identified pre-existing split socket or one
matching-safe contraction elsewhere.  Reversibility of a signed source
relation is not by itself such a contraction.

## 4. Common-cap obstruction

The script field `pointwise_common_cap=True` only forms coordinatewise
unions and checks that each phase letter is contained in that union.  A
legal source cap must additionally lie in the intersection of every owner
row using that source position.

At the newly exposed near position, the two phase letters contain opposite
active labels.  Their union contains all of `X`.  In the phase whose second
new row is `R_1`, that row omits the far active label by (3.2).  Hence the
coordinatewise union is not contained in the incident owner envelope.
Thus the two split endpoint words do not yet inhabit one pointwise
common-`Q` owner state.

This is an all-`d` obstruction to the same-address split.  It does not rule
out phase-private source positions, a nontrivial address permutation, or a
larger halo braid.  Any such escape must pass the maximal reconstruction
test for every owner, compiler, `q1` and protected row; containment of the
two displayed phase letters in an arbitrary set is insufficient.

## 5. Exact scope of the owner surgery

At owner-factor level, delete the host edge `UV`, a second edge `WY`, and a
forest-opening edge `AB`, and add `VW`.  The first upper loss is cancelled
because

\[
                         U\cup V=V\cup W.              \tag{5.1}
\]

The upper colours of `WY` and `AB` have spare occurrences, so all sixteen
upper **support values** remain.  The upper occurrence counter nevertheless
loses one `WY` occurrence and one `AB` occurrence.

The lower occurrence action is

\[
 -[U\cap V]-[W\cap Y]-[A\cap B]+[V\cap W].             \tag{5.2}
\]

Thus the surgery is not lower-`q1` palette preserving.  Its positive finite
claim is that the `8d+22` retained lower colours are distinct and the two
resulting paths are internally/clipped resident.  Exterior endpoint halos
and any exact lower-palette sidecars remain part of the ambient splice.

Most importantly, the common-endpoint and upper-safe-seam audits certify
different rows.  The former supplies one opposite suffix ray but has upper
support fifteen; the latter restores upper support sixteen but does not
certify the missing complementary prefix shore in the same cap/guard state.
They cannot be multiplied into a combined cross bank by set identities.

## 6. Corrected sufficient interface

The endpoint packet can be used without a separate background Hall theorem
under the following exact hypotheses.

1. The rethreaded typed source `B` is already physically embedded with the
   intended owner chronology and all upper/residence rows.
2. A literal old matching `M` is fixed, and every full-block lift under
   `B_0 -> (F,N)` is admissible with its complete width/address/guard record.
3. The new suffix-ray cells are side cells and their targets are not also
   demanded by the transported background bank.
4. A complementary prefix occurrence bank is supplied in the same complete
   cap/guard state, giving both cross perfect matchings of the zero-block
   theorem.
5. The owner-forest interfaces, the lower colours lost in (5.2), and the
   split's two nonflat rows are restored or explicitly accepted.
6. The split socket is recycled or one admissible contraction pays (3.4).

Under 1--3, full-block lifting alone transports the background matching.
Under 1--6, the local ray defect is zero and the true additive charge is the
certified reset charge.  Conditions 4--6 are open for the current endpoint
module.

## 7. Independent replay and hashes

The independent light replay reads the two frozen censuses, asserts (0.1),
checks the one-suffix-ray and upper-safe-forest rows, and verifies the
symbolic transport/facet formulas for `2<=d<=32`:

```text
scratch/audit_k_c8_endpoint_one_ray_background_chi_20260801.py
  SHA-256 d96f29dd66faf5bd0420d63a96756a76e88c5ea7ba6f6065ccd338519a043555

scratch/k_c8_endpoint_one_ray_background_chi_20260801.audit.json
  SHA-256 dc88a1dd58b91de0736cd83e35a75660a57caae06887c24a0cf29f502b9daa87
  payload 97a2c1a007bf487afd3a17b68e617de068c085a9ec2523ecc83508ef66cf4174
```

It binds the frozen payloads

```text
common endpoint: 9376d5e8c4b5b91e2609f7e440cb8096f66543804cb1da11018b276f00fdd49d
upper-safe seam: 7b0acdfafbf90610e7f8764517a2562ce1787adb594cf64a5ea5d8d1023cf848
```

and returns

```text
PASS_K_C8_ENDPOINT_ONE_RAY_SCOPE_CORRECTION
```

The audited construction note is
`MATH_THEOREM_C8_BOUNDARY_RAY_CROSSMATCH_FOREST_ACTUATOR_20260801.md`.
Its corrected status must be read as a one-ray theorem, not a combined-cross
or zero-charge theorem.
