# Independent audit of the all-r short-sector Johnson path

Date: 2026-09-08.
Reviewer: Codex subagent exact_b_finite_frontier.
Status: PASS, pure algebraic audit. No new program was run.

Reviewed:

    scratch/PBBS_ALL_R_SHORT_RUN_SECTOR_JOHNSON_PATH_20260908.md.

## 1. Exact representation and block endpoints

The boundary triples (b,r-2-b,0), b=0,...,r-3, represent distinct cyclic-triple classes and all classes containing a zero. The omitted endpoint b=r-2 is a cyclic rotation of b=0, so it must not be counted twice. The root u=n-1 gives exactly the displayed parity form for A_b.

From the established root map, f^3 rotates by one. A boundary triple has rotational period three and a unique physical root, hence f-period3n; because3n is odd, g=f^2 has the same period. Opening at c_b=2n-b gives last state g^(2n-b-1)A_b. The next block has exactly that exponent at its first state. The final nonzero block has last state f^(3n+5)A_(r-3)=f^5A_(r-3). These endpoint exponents and their off-by-one conventions are correct.

## 2. The three-condition seam criterion is exact

At a Johnson lower-owner seam, write L_0 minus R_0={a} and R_0 minus L_0={b}. For the complemented owners:

- a is newly positive on the right, so absence from R_1,R_2 is exactly the requirement that this new positive run reach length three;
- b is positive immediately to the left and absent on the right, so absence from L_1,L_2 is exactly the requirement that its terminal positive run reach length three;
- a coordinate absent from both lower seam endpoints is positive on both upper endpoints. Its only remaining short possibility is a two-position run, excluded by L_1 intersect R_1 being contained in L_0 union R_0;
- a coordinate present in both lower seam endpoints has no upper positive run touching the seam.

Thus the three tests are necessary and sufficient in the stated Johnson case. They agree with the five general forbidden-pattern containments in the note; no additional coordinate type is missing.

## 3. Independent phase calculation

Writing B_b=fA_b, C_b=f^2A_b and removing a common rotation, the six-state stencils are exactly:

    phase0: rho^-2 C_b, rho^-1 B_b, A_b
            | A_(b+1), C_(b+1), rho B_(b+1);

    phase1: rho^-1 A_b, rho^-1 C_b, B_b
            | B_(b+1), rho A_(b+1), rho C_(b+1);

    phase2: rho^-1 B_b, A_b, C_b
            | C_(b+1), rho B_(b+1), rho^2 A_(b+1).

These follow by reducing the six f-times t-4,t-2,t,t,t+2,t+4 modulo three, retaining their rotation factors. They are the same stencils given in the construction.

Put x=2b+1, y=2b+2, z=2b+3. The changed-coordinate checks are:

| phase | departure a | arrival b | reason the three-run flanks are legal |
|---:|---:|---:|---|
| 0 | x | y | x is absent from C_(b+1),rho B_(b+1); y is absent from rho^-1 B_b,rho^-2 C_b |
| 1 | y | x | y is absent from rho A_(b+1),rho C_(b+1); x is absent from rho^-1 C_b,rho^-1 A_b |
| 2 | z | y | z is absent from rho B_(b+1),rho^2 A_(b+1); y is absent from A_b,rho^-1 B_b |

For the remaining cross-intersection test:

- in phase0, only2r in R_1 can lie outside L_0 union R_0; it is not in rho^-1 B_b since0 is not in B_b;
- in phase1, onlyz in R_1 can lie outside the union; it is not in rho^-1 C_b since z+1=2b+4 is not in C_b;
- in phase2, onlyx in L_1 can lie outside the union; it is not in rho B_(b+1) since x-1=2b is not in B_(b+1).

Each parity assertion follows directly from the displayed inclusive intervals. The range1<=b<=r-4 keeps the potentially dangerous labels away from the cyclic endpoint, so no wraparound coordinate is silently omitted.

## 4. Final seam and small parameters

For the final seam, the six states in the construction are fA_(r-3), f^3A_(r-3), f^5A_(r-3) followed by A_0,f^2A_0,f^4A_0. Substitution into the parity formulas gives exactly its displayed final stencil.

The seam replaces2r-2 by2r-3. The former is absent from both right flank states, the latter from both left flank states. The only possible additional right-flank coordinate outside the seam union is2r, absent on the opposite left flank. Thus the three-condition criterion passes.

At r=4 the interval odds[1,2r-7] is the singleton{1}, so the smallest nontrivial final seam also has the stated stencil. At r=3 there is one block and no new seam. Empty parity intervals cause no hidden exception.

## 5. Source realization and scope

Every original bad-sector component is a Johnson cycle with no positive upper run shorter than three, by the established exact run classification. A run of length at most two cannot span two joins because each retained block has length3n>=21. Therefore checking each new seam suffices for the whole path.

The maximal depth-two factor intersects at most three consecutive rank-(r+1) Johnson owners. Its letters have size at least r-1>0. The run-length criterion then supplies exact owner replay. Hence the owner count, Johnson property, residence property, and literal shallow source theorem all follow.

The note correctly does NOT promote the finite r8 upper-support replay or facet injectivity to an all-r theorem. The all-dimensional result proved here is the explicit shallow-sector path and source only. The remaining upper-transport, full-factor integration, and lower-compiler gates are preserved.

No defect was found in the reviewed proof. This audit used no computation, search, or external theorem beyond the dependencies already stated in the construction.
