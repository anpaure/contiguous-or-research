# Independent audit of the ROTS stabilizer absorber and K17 round 4

**Date:** 2026-08-02  
**Status:** theorem audit PASS; K17 finite round is an independently replayed
negative calibration and does not supersede the deficit-89 baseline.

## 1. Stabilizer theorem audit

The proof was checked in the literal left/right-copy matching graph.

* Every named endpoint/history set is a union of atoms of the Boolean algebra
  it generates.  The product of symmetric groups on those atoms fixes the set,
  so protected endpoints are singleton refined orbits.
* Any invariant relation between two transitive refined orbits is biregular:
  the group maps the neighbor set of one vertex bijectively to that of any
  other vertex on the same shore.
* Subtracting the protected partial matching gives residual supplies
  \(s_i-p_i\) and capacities \(c_j-q_j\).  Uniform spreading on the biregular
  residual pairs gives a literal fractional matching; ordinary bipartite
  integrality gives an extension.
* The residual cut inequality expands exactly to
  \[
             q(N(X))-p(X)\leq c(N(X))-s(X).
  \]
* Protected charge is nonnegative because the protected matching injects the
  protected tails in \(X\) into protected heads in \(N(X)\).

The cut formula is bound to the full refined graph, retaining protected
singleton types with zero residual capacity, or directly to the same literal
shore.  It must not be applied after merging protected and unprotected
vertices into one count-only type.

The chronology obstruction follows: if an old shore has deficit \(\delta\),
then any successful reordered chronology must expose at least \(\delta\) new
right capacity.  Splitting types while retaining their old times leaves the
literal neighborhood unchanged and cannot repair the cut.

## 2. Absorber audit

The tight-cut criterion is sufficient.  On zero-slack cuts its hypothesis is
the exact residual Hall inequality.  On every positive-slack cut,
\[
              \chi_P(X)\leq|P|\leq\mu\leq\sigma(X).
\]

For the reserve splice, the disjointness condition is load-bearing:
\[
              Z\subseteq R\setminus(M(L)\cup R_P).
\]
With
\[
 A=\{\ell\notin L_P:M(\ell)\in R_P\},
\]
retain \(M\) off \(L_P\cup A\), use \(P\) on \(L_P\), and match \(A\) into
\(Z\).  The three right images are disjoint.  Omitting \(Z\cap R_P=\varnothing\)
would make the statement false.

The type-count bound \(2^{|H|}(k+1)^{2^r}\) is valid for \(r\) named sets.
It is polynomial only for bounded \(r\); it is not a uniform bounded-state
claim for \(r=O(d)\).

After chronology and protected literals are fixed, the residual max-flow and
the three-threshold interval reset flow are both totally unimodular.  The
first non-TU coupling is the common literal row selector; the three-resource
parity tensor supplies its determinant-two minor.  Integer
chronology/configuration master plus residual min-cut Benders cuts is
therefore the proof-safe decomposition.

## 3. K17 recoupled baseline

The authoritative builder-phase baseline remains:

\[
(n_1,n_2,n_3)=(0,7395,16915),\qquad
16809/16898,
\]

with deficiency \(89\), \(77\) zero hard heads, and Hall shore \(102/13\).
Its table, projection audit, Hall witness, and independent static replay
have SHAs

    62d711033eabeaa3ab60da93327a0bc6181cc6ac80dbf11b6ce997e616780ad6
    6aa2fd135371d7b9d3d7b47719cc2e47f39804d9c687822d35f29dd3e88f302c
    e55b88af317f3241912a96ef08ff3397dd2cc0693c3dca460b01dd30043b5892
    1f0b2a9876b2fc6160efb59564a5a887d8931fe2bf5e1373f326ca30d1d4719d

respectively.

## 4. New bounded round 4

One single-core H100 round was run under

    /home/amodo/or15/work/k_rots_minlong_cegar_round4_20260802

with seed \(2026080204\), core 63, nice 15, a 2 GiB virtual-memory cap, and
30-minute fail-closed timeouts.  No GPU or portfolio was used.

The builder independently reconstructs an exact-minlong table:

* 24,310 rows and 65,535 lower targets;
* every rank-at-most-eight target exactly once;
* lengths \(0,7395,16915\);
* the selected owner phase is a 24,310-edge perfect matching;
* one selected factor component.

The independent projection audit gives

\[
                     16723/16898,
\]

deficiency \(175\), \(152\) zero hard heads, and Hall shore \(202/27\).
Thus it is strictly worse than the baseline.

The builder was asked to shorten the baseline's 102 Hall heads.  The exact
singleton-to-donor containment matching selected zero of them:

\[
                         0/102.
\]

This is a proof-safe no-go only for removing those heads directly with the
current singleton-to-donor move.  Other recouplings may create new suppliers
for them.

Frozen local mirror:

    scratch/k_rots_minlong_cegar_round4_20260802

Principal SHAs:

    manifest                 377ed1069770c2a9dc3f1dca4b969ecfa9eb937507a9aeb0b8e82c69b57487a3
    table                    39dec63bd720cea7be3d23ef495b0448e47406c81a05fdc0319c304920eecbc7
    builder audit            6973b57bc379012099719de70681d587324a6f724c8ebc1a0f700528f5f4d005
    projection audit         ef3e4757fe7ee4e5f5a469700d6d7a2ad44ece04485140f5bf39c8d7b24052e7
    independent static audit 9334031af13b0204630d59c70da35999a744b9edbe09e8738a28fa3f6858b8d2
    Hall witness             9c78387bd69d088bf5dae3bf29d15a838d0875534f28b295ff7848521f5c6dac
    zero-head list           a181e0e1c81d382a4f2854bce24ea3159733361c7a5d65b8b9d4d6c22c5e2388

## 5. Exact next finite scope

The simple priority CEGAR is not a monotone descent and should not be
continued as a seed portfolio.  The next exact finite target is the joint
one-short ROTS projection:

1. choose all \(1748\) singleton-to-donor reroutes from the global
   \(401\,754\)-edge matching;
2. choose one literal address state per long and short role;
3. choose direct long arcs and common-literal-state hyperarcs
   long-to-short-to-long;
4. give every long role indegree and outdegree one and use every short once.

That projection fixes the reset sockets jointly.  SAT still requires cyclic
literal-cell replay; builder-phase UNSAT does not close the alternate owner
phase, and a fixed-table result does not close the global recoupling fibre.
