// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface GetPackerImageIterationBuild {
    /**
     * Name of the cloud provider this image is stored-in, if any.
     */
    cloudProvider: string;
    /**
     * Name of the builder that built this. Ex: 'amazon-ebs.example'.
     */
    componentType: string;
    /**
     * Creation time of this build.
     */
    createdAt: string;
    /**
     * HCP ID of this build.
     */
    id: string;
    images: outputs.GetPackerImageIterationBuildImage[];
    /**
     * Labels for this build.
     */
    labels: {[key: string]: string};
    /**
     * Packer generated UUID of this build.
     */
    packerRunUuid: string;
    /**
     * Status of this build. DONE means that all images tied to this build were successfully built.
     */
    status: string;
    /**
     * Time this build was last updated.
     */
    updatedAt: string;
}

export interface GetPackerImageIterationBuildImage {
    /**
     * Creation time of this iteration
     */
    createdAt: string;
    /**
     * The ID of this resource.
     */
    id: string;
    imageId: string;
    region: string;
}

