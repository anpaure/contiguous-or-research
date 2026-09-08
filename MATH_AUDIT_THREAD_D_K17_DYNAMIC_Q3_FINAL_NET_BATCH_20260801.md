# Exact dynamic q=3 final-net batch obstruction on the protected k=17 factor

Date: 2026-08-01  
Lane: Thread D; fixed authenticated seven-component factor  
Status: exact finite `NO_PASS` in the scope below

## 1. Scope

Let `F` be the authenticated protected incidence factor

`scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`

of SHA-256

`7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`.

It has seven components of owner sizes

`14305, 8615, 1362, 18, 4, 3, 3`,

and contains 52 protected incidences.  We consider an ordered sequence of
three standard incidence-C6 toggles.  At each step:

1. the three removed incidences are present and unprotected;
2. the complementary three incidences are absent;
3. the three removed incidences lie on three distinct *current* components.

Thus every step is a genuine fusion and the required component trajectory is

`7 -> 5 -> 3 -> 1`.

Unlike the earlier prefix-safe census, rank-10 holes are permitted after the
first and second toggle.  Only the final rank-10 multiplicities must all be
positive.  Candidate C6 phases are rebuilt after every toggle, so generated
incidences and overlapping supports are included.

## 2. Changed-incidence completeness lemma

Fix a current state obtained from the base factor by toggles, and call an
incidence **added** when it is current but was absent from the base factor.

**Lemma 2.1.** Every currently selected C6 phase is either selected already in
the base factor or contains an added incidence among its three old edges.

**Proof.** If all three old incidences belong to the base factor, their being
current says precisely that the same phase's old matching was selected in the
base factor.  Otherwise one old incidence is current and non-base, hence is
added.  This is exhaustive. `square`

Every Boolean rank-8/rank-9 incidence belongs to exactly 64 oriented old-side
C6 phases: choose one of the eight coordinates of the lower set to remove for
the rank-7 core and one of the eight coordinates outside the owner as the
third label.  Consequently the exact dynamic phase bank is obtained by

- filtering the 3,379 unprotected base phases supported on three base
  components, and
- adjoining the at most `64 a` phases indexed by the `a` current added
  incidences,

followed by literal presence, absence, protection, and current-component
tests.  Here `a <= 3` after one toggle and `a <= 6` after two toggles.

This is an exact index, not a neighbourhood heuristic.

## 3. Final-current pruning

A C6 toggle changes the rank-10 colour at exactly three lower vertices.  It
can therefore create at most three distinct new rank-10 providers.

**Lemma 3.1.** If a state with `t` toggles remaining has more than `3t`
rank-10 holes, no continuation by those toggles can be rank-10 exact.

The implementation maintains the exact sparse current

`base multiplicity + cumulative delta`

on every touched rank-10 colour.  For every enumerated first- and second-step
state this sparse count was independently compared with a literal full-factor
rank-10 replay.  Component counts were likewise replayed literally as five
and three.

## 4. Exact census

The calibrated base catalogue has:

- 4,667,520 oriented incidence hexagons;
- 46,960 selected phases;
- 46,818 protected-safe phases;
- 3,379 phases on three distinct base components.

The dynamic ordered search gives:

| quantity | exact value |
|---|---:|
| first fusion states | 3,379 |
| first states pruned by the six-hole bound | 0 |
| exact second-fusion candidates/states | 1,334 |
| second states with more than three holes | 432 |
| second states surviving the final-current bound | 902 |
| dynamically regenerated third-fusion candidates on those 902 states | **0** |
| final rank-10-exact sequences | **0** |

The exact rank-10 hole histograms are

- after step 1, for holes `0,1,2,3`: `405,1189,1361,424`;
- after step 2, for holes `0,1,2,3,4,5,6`:
  `12,118,306,466,318,106,8`.

Thus the obstruction occurs before residence or deeper-shadow optimization:
the 432 discarded states cannot repair their rank-10 current with one C6,
while the other 902 states have no legal third three-component C6 fusion at
all.

## 5. Theorem and exact limitation

**Theorem 5.1 (fixed-factor dynamic three-C6 no-go).** The authenticated
seven-component factor admits no protected ordered batch of three incidence-C6
fusions with component trajectory `7 -> 5 -> 3 -> 1` and rank-10-exact final
net current, even when intermediate rank-10 holes and dynamically generated
or overlapping C6 supports are allowed.

Because no final state exists, there is no final residence/rank-11--13 ticket
to attach.  This theorem does **not** exclude a preparatory neutral/splitting
move, a compound packet not sequentially expressible as three such fusions,
release of a protected incidence, a higher-q actuator, or a rebuilt host.
It makes no claim about compiler, voltage, or regeneration.

## 6. Reproducible artifacts

Remote root:

`/home/amodo/or15/work/threadD_k17_q3_final_net_batch_20260801`

Successful audited rerun PID: `3773376`, CPU 63, address-space cap 4 GiB,
CPU-time cap 3600 s.  It completed with exit status 0 in 10.44 wall seconds
and used 7,680 KiB maximum RSS.

Local bundle:

`scratch/threadD_k17_q3_final_net_batch_20260801/`

Hashes:

- source: `a7326db95fd823c570e36a1167837fb5580c9e2c35c3f62bcd05bbbff5f4dcdc`;
- audit JSON: `bb7083b4b954753b3d79b091b53522f5b8827a2b067041f5e99dcd79c5787cdb`;
- stdout: `574872bb9de43a2fd163848385e87d98aef4f48409213f3ee94c7546917dd42b`;
- stderr/timing: `e7442d8491309446de4275be4df360253cbff139824472e7a81c718f0a95a9d3`;
- no-witness factor marker:
  `7ac82badea021fe016a1b0a80954a28107912c112fca33d0311b82768f5cead0`.
